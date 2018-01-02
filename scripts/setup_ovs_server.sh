#!/usr/bin/env bash

sudo /usr/local/share/openvswitch/scripts/ovs-ctl start
sudo sysctl -w net.ipv4.ip_forward=1
sudo ovs-vsctl del-br br1
sudo ovs-vsctl add-br br1
sudo ovs-vsctl set-controller br1 tcp:35.193.107.149:8080
export ipv4_br=10.10.10.10
export mac_br=`ifconfig br1|grep 'HWaddr'| gawk 'match($0, /HWaddr (.*?)  /, ary) {print ary[1]}'`
sudo ifconfig br1 ${ipv4_br}/24 up

export router_ip0=172.31.19.159
export router_mac0=86:f1:ef:7d:de:06
sudo ovs-vsctl add-port br1 gre -- set interface gre type=gre options:remote_ip=${router_ip0}
sudo ovs-ofctl add-flow br1 priority=100,in_port=gre,actions=mod_nw_dst=${ipv4_br},mod_dl_dst=${mac_br},local
sudo ovs-ofctl add-flow br1 priority=100,in_port=local,actions=gre

sudo ip route add default dev br1 tab 2
sudo ip rule add from 10.10.10.10/24 tab 2
