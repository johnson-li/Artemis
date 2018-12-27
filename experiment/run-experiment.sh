#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"

./build.sh

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
