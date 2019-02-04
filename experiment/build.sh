#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"/..

cd ../ngtcp2
git pull
autoreconf -i
make -j$(nproc) > /dev/null
cd ../Hestia
git pull
cp ../ngtcp2/examples/balancer bin
cp ../ngtcp2/examples/client bin
cp ../ngtcp2/examples/server bin
cp ../ngtcp2/lib/.libs/libngtcp2.so.0 bin
cp ../openssl/libssl.so.1.1 bin
cp ../openssl/libcrypto.so.1.1 bin

cd ${old_dir}
