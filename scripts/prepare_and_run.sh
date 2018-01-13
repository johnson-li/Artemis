#!/usr/bin/env bash

host=$1
arch=$2
echo host: ${host}

cd ..
python3 -m hestia.experiment.main ${host}
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
    ./sync_planetlab_i386.sh ${host}
else
    cp ../udp-server/client server
    cp ../udp-server/simple_client server
    ./sync_planetlab.sh ${host}
fi;

./run_remote.sh ${ip}
