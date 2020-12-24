#!/bin/bash

# conda activate dev

# python -m experiment.gcloud.main2
# sleep 60
# python -m experiment.gcloud.restart2

echo The server is ready.

for i in `seq 4`
do
    python -m experiment.client.machines.aws.start --range $(((i-1)*4)),$((i*4))
    sleep 30
    python -m experiment.client.main
    item_count=$(mysql -ujohnson -pjohnson -D serviceid_db -sN -e 'select count(*) from transfer_time;')
    while (( $item_count < $((i*4*5)) )) && (( $item_count < 75 ))
    do
        sleep 10
        item_count=$(mysql -ujohnson -pjohnson -D serviceid_db -sN -e 'select count(*) from transfer_time;')
    done
    python -m experiment.client.machines.aws.cleanup
    sleep 5
done

