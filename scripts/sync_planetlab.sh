#!/usr/bin/env bash

USER_DIR=$PWD
BASE_DIR=$(dirname "$0")

cd ${BASE_DIR}

ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no goettingenple_txp1@$1 'mkdir ~/server'
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no server/client goettingenple_txp1@$1:~/server/client
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no server/simple_client goettingenple_txp1@$1:~/server/simple_client
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no conduct_exp1.sh goettingenple_txp1@$1:~/

cd ${USER_DIR}
