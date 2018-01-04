#!/usr/bin/env bash

host=$1
ip=`dig +short ${host}`

cd ..
python -m hestia.experiment.main ${ip}
cd scripts

./sync_planetlab.sh ${host}
./run_remote.sh ${ip}
