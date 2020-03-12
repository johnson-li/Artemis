date > ~/start_server.sh.start_ts

unicast=`python3 -c 'import socket; import os; import json; machines=json.load(open("machine.json")); print(machines[socket.gethostname()]["external_ip1"])'`
sudo LD_LIBRARY_PATH=~/data ~/data/server --interface=ens4 --unicast=${unicast} 0.0.0.0 4433 ~/data/server.key ~/data/server.crt

date > ~/start_server.sh.end_ts
