#!/usr/bin/env bash

TIMEOUT_CMD=timeout
if [ `uname` = 'Darwin' ]
then
    TIMEOUT_CMD=gtimeout
fi

if [ -z ${repeat+x} ]
then
    repeat=30
fi
echo repeat: ${repeat}

USER_DIR=$PWD
BASE_DIR=$(dirname "$0")

cd ${BASE_DIR}

#direct_server=''
#dns_servers=''
#sid_router=''
self_ip=$1
echo self: ${self_ip}
sid_server=`sqlite3 ../resources/db/sip.db "select server from sip where host = '${self_ip}'"`
direct_data=''
dns_data=''
sid_data=''

# Direct query
direct_server=`dig +short cdn.xuebing.name`
#direct_server=127.0.0.1
for i in `seq ${repeat}`
do
    output=`${TIMEOUT_CMD} 2 ./server/simple_client ${direct_server}| grep cost| egrep -o '[0-9]+'`
    if [ -z "$output" ]
    then
        output=0
    fi
    direct_data=${direct_data},${output}
done
echo direct_data: ${direct_data}

# Dns query
for i in `seq ${repeat}`
do
    dns_server=`dig +short cdn${i}.xuebing.name`
#    dns_server=127.0.0.1
    dns_servers=${dns_servers},${dns_server}
    output=`${TIMEOUT_CMD} 2 ./server/simple_client ${dns_server}| grep cost| egrep -o '[0-9]+'`
    if [ -z "$output" ]
    then
        output=0
    fi
    dns_data=${dns_data},${output}
done
echo dns_data: ${dns_data}

# SID query
sid_router=`dig +short sid.xuebing.name`
for i in `seq ${repeat}`
do
    output=`${TIMEOUT_CMD} 2 ./server/client ${sid_router} ${sid_server}| grep cost| egrep -o '[0-9]+'`
    if [ -z "$output" ]
    then
        output=0
    fi
    sid_data=${sid_data},${output}
done
echo sid_data: ${sid_data}


# print server IPs
echo direct_server: ${direct_server}
echo dns_servers: ${dns_servers}
echo sid_router: ${sid_router}
echo sid_server: ${sid_server}

cd ${USER_DIR}

