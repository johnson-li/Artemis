date >setup.sh.start_ts

iface_secondary='ens5'
var=$(ifconfig ${iface_secondary} | grep ether)
# vars=("$var")
# mac_secondary=${vars[1]}
ip_primary=$(python3 -c 'import json; machines=json.load(open("machine.json")); print(machines[machines["hostname"]]["internal_ip1"])')
ip_secondary=$(python3 -c 'import json; machines=json.load(open("machine.json")); print(machines[machines["hostname"]]["internal_ip2"])')

sudo iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP
for bridge in $(sudo ovs-vsctl show | grep Bridge | sed -E 's/ +Bridge //' | sed -E 's/"//g'); do
  sudo ovs-vsctl del-br "$bridge"
done

hostname=$(python3 -c 'import json; machines=json.load(open("machine.json")); print(machines["hostname"])')
region=${hostname:0:$((${#hostname} - 7))}
all_hosts=$(python3 -c 'import json; machines=json.load(open("machine.json")); machines = [k for k in machines.keys() if k.endswith("server")]; print(",".join(machines))')

# Setup GRE tunnels
sudo ovs-vsctl add-br bridge
# var=$(ifconfig bridge | grep ether)
# vars=("$var")
# mac_bridge=${vars[1]}
# server_ip=$(python3 -c 'import os; import json; machines=json.load(open("machine.json")); print(machines[os.environ["server"]]["internal_ip1"])')

# Create ports
sudo ovs-vsctl add-port bridge $iface_secondary
sudo ovs-vsctl add-port bridge server -- set interface server type=internal
sudo ovs-vsctl add-port bridge router -- set interface router type=internal
sudo ovs-ofctl del-flows bridge

# Setup NICs
sudo ifconfig bridge "$ip_secondary/24" up
sudo ifconfig server 12.12.12.12/32 up
sudo ifconfig router 12.12.12.12/32 up

# Create flows
sudo ovs-ofctl add-flow bridge in_port=local,actions="$iface_secondary"
sudo ovs-ofctl add-flow bridge in_port="$iface_secondary",actions=local
sudo ovs-ofctl add-flow bridge in_port=server,actions=router
sudo ovs-ofctl add-flow bridge in_port=router,actions="${iface_secondary}"

# Setup ARP
sudo arp -s "$ip_primary" 00:00:00:00:00:00 -i router
sudo arp -s "$ip_secondary" 00:00:00:00:00:00 -i router
sudo arp -s 12.12.12.12 -i router
sudo arp -s 12.12.12.12 -i server

# Setup remote routers
while IFS=',' read -ra ADDR; do
  for remote_host in "${ADDR[@]}"; do
    dc_region=${remote_host:0:$((${#remote_host} - 7))}
    if [[ "$dc_region" != "$region" ]]; then
      export remote_host
      export dc_region_short=${dc_region:7}
      remote_ip=$(python3 -c 'import os; import json; machines=json.load(open("machine.json")); print(machines[os.environ["remote_host"]]["external_ip1"])')
      dc_region_short=$(python3 -c "import os; print('-'.join([''.join((t[:2], t[-2:])) for t in '${dc_region_short}'.split('-')[:2]]))")
      local_port_name=$dc_region_short
      remote_port_name=t-${dc_region_short}
      sudo ovs-vsctl add-port bridge "${local_port_name}" -- set interface "${local_port_name}" type=internal
      sudo ovs-vsctl add-port bridge "${remote_port_name}" -- set interface "${remote_port_name}" type=vxlan options:remote_ip="${remote_ip}"
      sudo ifconfig "${local_port_name}" 12.12.12.12/32 up
      sudo ovs-ofctl add-flow bridge in_port="${local_port_name}",actions="${remote_port_name}"
      sudo ovs-ofctl add-flow bridge in_port="${remote_port_name}",actions="${local_port_name}"
      sudo arp -s "$ip_secondary" 00:00:00:00:00:00 -i server
      sudo arp -s "$ip_secondary" 00:00:00:00:00:00 -i router
      sudo arp -s "$ip_secondary" 00:00:00:00:00:00 -i "$local_port_name"
    fi
  done
done <<<"$all_hosts"

date >setup.sh.end_ts
