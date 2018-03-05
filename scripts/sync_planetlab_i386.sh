#!/usr/bin/env bash

USER_DIR=$PWD
BASE_DIR=$(dirname "$0")

cd ${BASE_DIR}

ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no goettingenple_txp1@$1 'mkdir ~/server'
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no server-i386/client goettingenple_txp1@$1:~/server/client
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no server-i386/simple_client goettingenple_txp1@$1:~/server/simple_client
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no conduct_exp1_direct.sh goettingenple_txp1@$1:~/
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no conduct_exp1_hit.sh goettingenple_txp1@$1:~/
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no conduct_exp1_miss.sh goettingenple_txp1@$1:~/
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no conduct_exp1_sid.sh goettingenple_txp1@$1:~/
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no timeout.sh goettingenple_txp1@$1:~/

cd ${USER_DIR}
