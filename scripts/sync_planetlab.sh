#!/usr/bin/env bash

USER_DIR=$PWD
BASE_DIR=$(dirname "$0")

cd ${BASE_DIR}

scp -r server goettingenple_txp1@$1:~/server
scp conduct_exp1.sh goettingenple_txp1@$1:~/

cd ${USER_DIR}
