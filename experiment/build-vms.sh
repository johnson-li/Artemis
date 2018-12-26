#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"/..

cd resources/vagrant
vagrant destroy -f
vagrant up

cd $old_dir

