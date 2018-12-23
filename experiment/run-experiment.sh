#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"
./build-images.sh
cd ${old_dir}

