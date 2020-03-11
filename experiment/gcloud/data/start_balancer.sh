hostname=`hostname`
zone=${hostname:0:`expr ${#hostname} - 7`}
sudo LD_LIBRARY_PATH=~/data ~/data/balancer --datacenter ${zone} bridge 0.0.0.0 4433 ~/data/server.key ~/data/server.crt

