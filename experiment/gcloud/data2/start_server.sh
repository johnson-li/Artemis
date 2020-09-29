date > ~/start_server.sh.start_ts

hostname=`hostname`
zone=${hostname:0:`expr ${#hostname} - 7`}
export zone=${zone:7}
zone=`python3 -c "import os; print('-'.join([''.join((t[:2], t[-2:])) for t in '${zone}'.split('-')[:2]]))"`
unicast=$(python3 -c 'import socket; import os; import json; machines=json.load(open("machine.json")); print(machines[socket.gethostname()]["external_ip1"])')
sudo LD_LIBRARY_PATH=~/data2 ~/data2/server_transport --user johnson --password johnson --datacenter ${zone} --unicast_nic=ens4 --anycast_nic=bridge "$unicast" 4433 4434 ~/data2/server.key ~/data2/server.crt

date > ~/start_server.sh.end_ts
