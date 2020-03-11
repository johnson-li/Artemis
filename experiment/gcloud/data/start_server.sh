var=`ifconfig ens4|grep 'inet '`
vars=( $var  )
unicast="${vars[1]}"
sudo LD_LIBRARY_PATH=~/data ~/data/server --interface=ens4 --unicast=${unicast} 0.0.0.0 4433 ~/data/server.key ~/data/server.crt

