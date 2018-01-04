#!/usr/bin/env bash

USER_DIR=$PWD
BASE_DIR=$(dirname "$0")

cd ${BASE_DIR}

output=`../udp-server`

cd ${USER_DIR}

