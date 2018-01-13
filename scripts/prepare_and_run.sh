#!/usr/bin/env bash

host=$1
echo host: ${host}
python3 -m hestia.experiment.main ${host}
ip=`dig +short ${host}| tail -n1`
sid_server=`sqlite3 ../resources/db/sip.db "select server from sip where host = '${ip}'"`

if [[ -z ${sid_server} ]]
then
    cd ..
    python -m hestia.experiment.main ${ip}
    cd scripts
fi

cp ../udp-server/client server
cp ../udp-server/simple_client server
./sync_planetlab.sh ${host}
./run_remote.sh ${ip}
