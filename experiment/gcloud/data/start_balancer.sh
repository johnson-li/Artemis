date > ~/start_balancer.sh.start_ts

hostname=`hostname`
zone=${hostname:0:`expr ${#hostname} - 7`}
zone=${zone:7}
zone=`echo $zone| sed -E 's/-//g'`
sudo LD_LIBRARY_PATH=~/data ~/data/balancer --datacenter ${zone} --user johnson --password johnson bridge 0.0.0.0 4433 ~/data/server.key ~/data/server.crt

date > ~/start_balancer.sh.end_ts
