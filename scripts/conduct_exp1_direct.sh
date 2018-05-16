#!/usr/bin/env bash

USER_DIR=$PWD
BASE_DIR=$(dirname "$0")
cd ${BASE_DIR}

region=$1

if [ -z ${repeat+x} ]
then
    repeat=20
fi
echo repeat: ${repeat}

direct_server=`sudo ping cdn${region}.xuebingli.com -c3 -W 4|grep PING| head -n1| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
for i in `seq ${repeat}`
do
    output=`sudo ./server/client ${direct_server}| grep cost| egrep -o '[0-9.]+'`
    if [ -z "$output" ]
    then
        output=0
    fi
    direct_data=${direct_data},${output}
done
echo direct_server: ${direct_server}
echo direct_data: ${direct_data}

cd ${USER_DIR}
