#!/usr/bin/env bash

source ./.venv/bin/activate
pip install --upgrade pip
pip install -qr requirements.txt
python -m hestia.system.main
