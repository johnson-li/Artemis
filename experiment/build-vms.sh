#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"/..

cd resources/vagrant
# vagrant destroy -f
# vagrant up --parallel
vagrant reload

cd ${old_dir}
