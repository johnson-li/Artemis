date > setup.sh.start_ts

iface_primary='en4'
iface_secondary='en5'
ip_primary=''
ip_secondary=''

sudo iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP
for bridge in `sudo ovs-vsctl show| grep Bridge| sed -E 's/ +Bridge //'| sed -E 's/"//g'`;
	do sudo ovs-vsctl del-br $bridge;
done

machines=`cat machine.json`

hostname=`python3 -c 'import json; machines=json.load(open("machine.json")); print(machines["hostname"])'`
all_hosts=`python3 -c 'import json; machines=json.load(open("machine.json")); machines.pop("hostname", None); print(",".join(machines.keys()))'`

setup_server() {
    # Setup the grep tunnel from server -> router
    router=''
    router_primary_ip_inner=''
    router_secondary_ip_outer=''
    router_bridge_name=$router
    router_port_name=tunnel-$router
    router_ip=$router_primary_ip_inner
    router_anycast_ip=$router_secondary_ip_outer
    router_anycast_mac=00:00:00:00
    sudo ovs-vsctl add-br $router_bridge_name
    sudo ovs-vsctl add-port $router_bridge_name $router_port_name -- set interface $router_port_name type=gre, options:remote_ip=$router_ip
    router_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $router_port_name| tail -n1| egrep -o "[0-9]+"`
    sudo ifconfig $router_port_name $router_anycast_ip/32 up
    sudo ovs-ofctl del-flows $router_bridge_name
    sudo ovs-ofctl add-flow $router_bridge_name in_port=$router_port,actions=mod_dl_dst:$router_anycast_mac,local
    sudo ovs-ofctl add-flow $router_bridge_name in_port=$local,actions=$router_port
}

setup_router() {
	sudo ovs-vsctl add-br bridge
	sudo ovs-vsctl add-port bridge $iface_secondary
	sudo ovs-vsctl del-flows bridge
	sudo ifconfig bridge $ip_secondary/24 up
	anycast_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $iface_secondary| tail -n1| egrep -o "[0-9]+"`
	sudo ovs-ofctl add-flow bridge in_port=local,actions=$anycast_port
	sudo ovs-ofctl add-flow bridge in_port=$anycast_port,actions=local

    # Setup the gre tunnel among routers
    while IFS=',' read -ra ADDR
    do
        for host in "${ADDR[@]}"
        do
            echo host
        done
    done <<< $all_hosts

    # Setup the gre tunnel from router -> server
	server=''
    server_ip=''
	server_gre_port_name=tunnel-$server
    sudo ovs-vsctl add-port bridge $server -- set interface $server_gre_port_name type=internal
	server_gre_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $server_gre_port_name| tail -n1| egrep -o "[0-9]+"`
	server_local_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface $server| tail -n1| egrep -o "[0-9]+"`
	sudo ovs-vsctl add-port bridge $server_gre_port_name -- set interface $server_gre_port_name type=gre, option:remote_ip=$server_ip
	sudo ovs-ofctl add-flow bridge in_port=$server_gre_port, actions=mod_dl_dst:,$server_local_port
	sudo ovs-ofctl add-flow bridge in_port=$server_local_port,actions=$server_gre_port
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

