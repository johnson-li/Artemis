#!/usr/bin/env bash

sudo /usr/local/share/openvswitch/scripts/ovs-ctl start
sudo sysctl -w net.ipv4.ip_forward=1
#sudo ovs-vsctl del-br br1
sudo ovs-vsctl add-br br1
sudo ovs-vsctl set-controller br1 tcp:35.193.107.149:6653
export ipv4_0=`ifconfig eth0|grep 'inet addr'| gawk 'match($0, /inet addr:(.*?)  Bcast/, ary) {print ary[1]}'`
export ipv4_1=`ifconfig eth1|grep 'inet addr'| gawk 'match($0, /inet addr:(.*?)  Bcast/, ary) {print ary[1]}'`
export ipv6=`ifconfig eth1|grep 'Global'| gawk 'match($0, /inet6 addr: (.*?) Scope/, ary) {print ary[1]}'`
export mac_eth=`ifconfig eth1|grep 'HWaddr'| gawk 'match($0, /HWaddr (.*?)  /, ary) {print ary[1]}'`
export mac_br=`ifconfig br1|grep 'HWaddr'| gawk 'match($0, /HWaddr (.*?)  /, ary) {print ary[1]}'`
export gateway=`route -n| gawk 'match($0, /0\.0\.0\.0 +([0-9.]+).*eth0/, ary) {print ary[1]}'| head -n1`
sudo ifconfig br1 ${ipv4_1}/24 up
sudo ifconfig br1 inet6 add ${ipv6}
sudo ovs-vsctl add-port br1 eth1
sudo ifconfig eth1 0
#sudo ovs-ofctl add-flow br1 priority=100,in_port=eth1,actions=mod_dl_dst:${mac_br},local
#sudo ovs-ofctl add-flow br1 priority=100,in_port=local,actions=mod_dl_src:${mac_eth},eth1

export server_ip0=172.31.31.148
#export server_ip1=172.31.2.200
sudo ovs-vsctl add-port br1 gre_server -- set interface gre_server type=gre options:remote_ip=${server_ip0}
#sudo ovs-ofctl add-flow br1 priority=200,udp,tp_dst=80,in_port=eth1,actions=gre


#sudo ip route add default via ${gateway} dev br1 tab 2
#sudo ip rule add from ${ipv4_1}/24 tab 2 priority 600