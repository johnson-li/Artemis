#!/usr/bin/env bash

USER_DIR=$PWD
BASE_DIR=$(dirname "$0")
cd ${BASE_DIR}

sid_server=$1

if [ -z ${repeat+x} ]
then
    repeat=10
fi
echo repeat: ${repeat}

sid_router=`sudo ping cdn.xuebing.name -w2|grep PING| head -n1| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
for i in `seq ${repeat}`
do
    output=`sudo ./server/client ${sid_router} ${sid_server}| grep cost| egrep -o '[0-9.]+'`
    if [ -z "$output" ]
    then
        output=0
    fi
    sid_data=${sid_data},${output}
done
echo sid_data: ${sid_data}
echo sid_server: ${sid_server}
echo sid_router: ${sid_router}


cd ${USER_DIR}
