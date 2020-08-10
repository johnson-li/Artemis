date > ~/start_balancer.sh.start_ts

hostname=$(hostname)
zone=${hostname:0:$(( ${#hostname} - 7))}
export zone=${zone:7}
zone=$(python3 -c "import os; print('-'.join([''.join((t[:2], t[-2:])) for t in '${zone}'.split('-')[:2]]))")
sudo LD_LIBRARY_PATH=~/data2 ~/data2/balancer2 --datacenter "$zone" --user johnson --password johnson bridge 0.0.0.0 4433 ~/data2/server.key ~/data2/server.crt

date > ~/start_balancer.sh.end_ts
