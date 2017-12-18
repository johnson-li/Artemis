#!/usr/bin/env bash

sudo sh -c "echo 'auto eth1\niface eth1 inet dhcp\niface eth1 inet6 dhcp' >> /etc/network/interfaces.d/50-cloud-init.cfg"

sudo sysctl -w net.ipv6.conf.all.forwarding=1

sudo /usr/local/share/openvswitch/scripts/ovs-ctl start

sudo ovs-vsctl add-br br1
sudo ovs-vsctl add-port br1 eth1

ipv4=`ifconfig eth1|grep 'inet addr'| gawk 'match($0, /inet addr:(.*?)  Bcast/, ary) {print ary[1]}'`
ipv6=`ifconfig eth1|grep 'Global'| gawk 'match($0, /inet6 addr: (.*?) Scope/, ary) {print ary[1]}'`
mac_eth=`ifconfig eth1|grep 'HWaddr'| gawk 'match($0, /HWaddr (.*?)  /, ary) {print ary[1]}'`
mac_br=`ifconfig br1|grep 'HWaddr'| gawk 'match($0, /HWaddr (.*?)  /, ary) {print ary[1]}'`
sudo ifconfig br1 ${ipv4}/20 up
sudo ifconfig br1 inet6 add ${ipv6}

sudo ovs-ofctl add-flow br1 priority=100,in_port=eth1,actions=mod_dl_dst:${mac_br},local
sudo ovs-ofctl add-flow br1 priority=100,in_port=local,actions=mod_dl_src:${mac_eth},eth1

gre_target=''
sudo ovs-vsctl add-port br1 gre -- set interface gre type=gre options:remote_ip=${gre_target}

server_ip=''
sudo ovs-ofctl add-flow br1 priority=500,in_port=gre,udp6,actions=set_field:${server_ip}-\>ipv6_dst,grs
sudo ovs-ofctl add-flow br1 priority=300,ipv6,udp,in_port=eth1,actions=gre

server_v4=''
sudo ovs-vsctl add-port br1 grs -- set interface grs type=gre options:remote_ip=${server_v4}

gateway_ip=''
sudo ovs-vsctl add-port br1 grg -- set interface grg type=gre options:remote_ip=${gateway_ip}
sudo ovs-ofctl add-flow br1 priority=200,in_port=grg,actions=mod_dl_dst:${mac_br},local