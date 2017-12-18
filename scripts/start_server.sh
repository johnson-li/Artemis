#!/usr/bin/env bash

if [ ! -d "/tmp/quic-data" ]; then
    mkdir /tmp/quic-data
    cd /tmp/quic-data
    wget -p --save-headers https://www.example.org
    cd -
fi

sudo ./quic_server --quic_response_cache_dir=/tmp/quic-data/www.example.org --certificate_file=leaf_cert.pem --key_file=leaf_cert.pkcs8 --port=80 --v=1