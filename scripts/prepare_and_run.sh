#!/usr/bin/env bash

host=$1
arch=$2
echo host: ${host}

cd ..
python3 -m hestia.experiment.main --peer ${host}
cd scripts

ip=`dig +short ${host}| tail -n1`
sid_server=`sqlite3 ../resources/db/sip.db "select server from sip where host = '${ip}'"`

if [[ -z ${sid_server} ]]
then
    cd ..
    python -m hestia.experiment.main ${ip}
    cd scripts
fi

if [ "$arch" = "32" ]; then
    cp ../udp-server/i686/client server-i386
    cp ../udp-server/i686/simple_client server-i386
    ./sync_planetlab_i386.sh ${host}
else
    cp ../udp-server/client server
    cp ../udp-server/simple_client server
    ./sync_planetlab.sh ${host}
fi;

./run_remote.sh ${ip}
