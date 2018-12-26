#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"/..

cd ../ngtcp2
git checkout -- .
git pull
make -j$(nproc) > /dev/null
cd ../Hestia
git checkout -- .
git pull
cp ../ngtcp2/examples/balancer bin
cp ../ngtcp2/examples/client bin
cp ../ngtcp2/examples/server bin
cp ../ngtcp2/lib/.libs/libngtcp2.so.0 bin
cp ../openssl/libssl.so.1.1 bin
cp ../openssl/libcrypto.so.1.1 bin

# ./experiment/build-images.sh
./experiment/build-vms.sh

python3 -m venv .venv
#virtualenv .venv

source ./.venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m hestia.system.main
deactivate

cd ${old_dir}
