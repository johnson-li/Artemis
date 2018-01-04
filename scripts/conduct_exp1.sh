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
sid_server=$1
direct_data=''
dns_data=''
sid_data=''

# Direct query
# direct_server=`dig +short cdn.xuebing.name`
direct_server=`sudo ping cdn.xuebing.name -c3 -W 4|grep icmp_seq| head -n1| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
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
#    dns_server=127.0.0.1
    output=`${TIMEOUT_CMD} 2 ./server/simple_client cdn${i}.xuebing.name| grep cost| egrep -o '[0-9]+'`
    # dns_server=`dig +short cdn${i}.xuebing.name`
    dns_server=`sudo ping cdn${i}.xuebing.name -c3 -W 4|grep icmp_seq| head -n1| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
    dns_servers=${dns_servers},${dns_server}
    if [ -z "$output" ]
    then
        output=0
    fi
    dns_data=${dns_data},${output}
done
echo dns_data: ${dns_data}

# SID query
# sid_router=`dig +short sid.xuebing.name`
sid_router=`sudo ping sid.xuebing.name -w2|grep PING| head -n1| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
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

