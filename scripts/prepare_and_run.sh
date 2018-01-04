#!/usr/bin/env bash

host=$1
ip=`dig +short ${host}`
sid_server=`sqlite3 ../resources/db/sip.db "select server from sip where host = '${ip}'"`

if [ -z ${ip} ]
then
    cd ..
    python -m hestia.experiment.main ${ip}
    cd scripts
fi

./sync_planetlab.sh ${host}
./run_remote.sh ${ip}
