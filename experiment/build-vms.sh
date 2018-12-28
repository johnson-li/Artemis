#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"/..

cd resources/vagrant
if [[ ! -z "$destroy" ]]
then
    echo 'full reload'
    vagrant destroy -f
    vagrant up --parallel
else
    echo 'partial reload'
    vagrant reload
fi

cd ${old_dir}
