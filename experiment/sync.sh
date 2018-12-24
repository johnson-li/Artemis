#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"/..

rsync -r experiment hestia resources gcp0:~/Workspace/Hestia

cd ${old_dir}
