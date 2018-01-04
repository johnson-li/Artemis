#!/usr/bin/env bash

USER_DIR=$PWD
BASE_DIR=$(dirname "$0")

cd ${BASE_DIR}

ssh goettingenple_txp1@$1 'mkdir ~/server'
scp server/client goettingenple_txp1@$1:~/server/client
scp server/simple_client goettingenple_txp1@$1:~/server/simple_client
scp conduct_exp1.sh goettingenple_txp1@$1:~/

cd ${USER_DIR}
