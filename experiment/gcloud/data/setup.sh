date > setup.sh.start_ts

iface_primary='ens4'
iface_secondary='ens5'
ip_primary=`python3 -c 'import json; machines=json.load(open("machine.json")); print(machines[machines["hostname"]]["internal_ip1"])'`
ip_secondary=`python3 -c 'import json; machines=json.load(open("machine.json")); print(machines[machines["hostname"]]["internal_ip2"])'`

sudo iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP
for bridge in `sudo ovs-vsctl show| grep Bridge| sed -E 's/ +Bridge //'| sed -E 's/"//g'`;
    do sudo ovs-vsctl del-br $bridge;
done

machines=`cat machine.json`

hostname=`python3 -c 'import json; machines=json.load(open("machine.json")); print(machines["hostname"])'`
region=${hostname:0:`expr ${#hostname} - 7`}
all_hosts=`python3 -c 'import json; machines=json.load(open("machine.json")); machines.pop("hostname", None); print(",".join(machines.keys()))'`

setup_server() {
    # Setup the grep tunnel from server -> router
    export router=${hostname:0:`expr ${#hostname} - 6`}router
    router_primary_ip_inner=`python3 -c 'import os; import json; machines=json.load(open("machine.json")); print(machines[os.environ["router"]]["internal_ip1"])'`
    router_secondary_ip_inner=`python3 -c 'import os; import json; machines=json.load(open("machine.json")); print(machines[os.environ["router"]]["internal_ip2"])'`
    router_bridge_name=router
    router_port_name=tunnel-router
    router_ip=$router_primary_ip_inner
    router_anycast_ip=$router_secondary_ip_inner
    router_anycast_mac=00:00:00:00:00:00
    sudo ovs-vsctl add-br $router_bridge_name
    sudo ovs-vsctl add-port $router_bridge_name $router_port_name -- set interface $router_port_name type=gre, options:remote_ip=$router_ip
    router_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $router_port_name| tail -n1| egrep -o "[0-9]+"`
    sudo ifconfig $router_bridge_name $router_anycast_ip/32 up
    sudo ovs-ofctl del-flows $router_bridge_name
    sudo ovs-ofctl add-flow $router_bridge_name in_port=$router_port,actions=mod_dl_dst:$router_anycast_mac,local
    sudo ovs-ofctl add-flow $router_bridge_name in_port=local,actions=$router_port
    sudo arp -s $router_primary_ip_inner 00:00:00:00:00:00 -i $router_bridge_name
    sudo ip route add default via $router_primary_ip_inner dev $router_bridge_name tab 2
    sudo ip rule add from $router_primary_ip_inner/32 tab 2 priority 600
}

setup_router() {
    bridge_name=bridge
    sudo ovs-vsctl add-br $bridge_name
    sudo ovs-vsctl add-port $bridge_name $iface_secondary
    sudo ovs-ofctl del-flows $bridge_name
    sudo ifconfig $bridge_name $ip_secondary/24 up
    anycast_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $iface_secondary| tail -n1| egrep -o "[0-9]+"`
    sudo ovs-ofctl add-flow $bridge_name in_port=local,actions=$anycast_port
    sudo ovs-ofctl add-flow $bridge_name in_port=$anycast_port,actions=local
    sudo ifconfig $iface_secondary down

    echo $all_hosts
    # Setup the gre tunnel among routers
    while IFS=',' read -ra ADDR
    do
        for remote_host in "${ADDR[@]}"
        do
            dc_region=${remote_host:0:`expr ${#remote_host} - 7`}
            type=${remote_host:`expr ${#remote_host}` - 6:6}
            if [[ ${type} == router ]] && [[ ${dc_region} != ${region} ]]
            then
                export remote_host
                remote_ip=`python3 -c 'import os; import json; machines=json.load(open("machine.json")); print(machines[os.environ["remote_host"]]["external_ip1"])'`
                local_port_name=$dc_region
                remote_port_name=tunnel-${dc_region}
                sudo ovs-vsctl add-port $bridge_name ${dc_region} -- set interface ${dc_region} type=internal
                sudo ovs-vsctl add-port $bridge_name ${remote_port_name} -- set interface ${remote_port_name} type=gre options:remote_ip=${remote_ip}
                local_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $local_port_name| tail -n1| egrep -o "[0-9]+"`
                remote_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $remote_port_name| tail -n1| egrep -o "[0-9]+"`
                sudo ifconfig ${local_port} 12.12.12.12/32 up
                sudo ovs-vsctl add-flow ${bridge_name} in_port=${local_port},actions=${remote_port}
                sudo ovs-vsctl add-flow ${bridge_name} in_port=${remote_port},actions=${local_port}
                sudo arp -s $ip_primary 00:00:00:00:00:00 -i ${local_port}
            fi
        done
    done <<< $all_hosts

    # Setup the gre tunnel from router -> server
    export server=${hostname:0:`expr ${#hostname} - 6`}server
    server_ip=`python3 -c 'import os; import json; machines=json.load(open("machine.json")); print(machines[os.environ["server"]]["internal_ip1"])'`
    server_local_port_name=server
    server_gre_port_name=tunnel-server
    sudo ovs-vsctl add-port $bridge_name $server_local_port_name -- set interface $server_local_port_name type=internal
    sudo ovs-vsctl add-port $bridge_name $server_gre_port_name -- set interface $server_gre_port_name type=gre, option:remote_ip=$server_ip
    server_gre_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $server_gre_port_name| tail -n1| egrep -o "[0-9]+"`
    server_local_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $server_local_port_name| tail -n1| egrep -o "[0-9]+"`
    sudo ovs-ofctl add-flow $bridge_name in_port=$server_gre_port,actions=mod_dl_dst:00:00:00:00:00:00,$server_local_port
    sudo ovs-ofctl add-flow $bridge_name in_port=$server_local_port,actions=$server_gre_port
    sudo arp -s $ip_primary 00:00:00:00:00:00 -i $server_local_port
}

for bridge in `sudo ovs-vsctl show| grep Bridge| sed -E 's/ +Bridge //'| sed -E 's/"//g'`
do
    sudo ovs-vsctl del-br $bridge
done

if [[ $hostname == *server ]]
then
    setup_server
fi
if [[ $hostname == *router ]]
then
    setup_router
fi

date > setup.sh.end_ts

