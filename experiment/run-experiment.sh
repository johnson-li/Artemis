#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"/..

./experiment/build-images.sh

python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
python -m hestia.system.main
deactivate

cd ${old_dir}
