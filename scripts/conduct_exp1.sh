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
dns_delay=''

# Direct query
# direct_server=`dig +short cdn.xuebing.name`
direct_server=`sudo ping cdn.xuebing.name -c3 -W 4|grep icmp_seq| head -n1| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
#direct_server=127.0.0.1
for i in `seq ${repeat}`
do
    output=`./server/simple_client ${direct_server}| grep cost| egrep -o '[0-9]+'`
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
    output=`./server/simple_client cdn${i}.xuebing.name`
    cost=`echo "${output}"| grep cost| egrep -o '[0-9]+'`
    dns_cost=`echo "${output}"| grep 'DNS delay'| egrep -o '[0-9]+'`
    dns_delay=${dns_delay},${dns_cost}
    dns_server=`sudo ping cdn${i}.xuebing.name -c3 -W 4|grep icmp_seq| head -n1| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
    dns_servers=${dns_servers},${dns_server}
    if [ -z "$cost" ]
    then
        cost=0
    fi
    dns_data=${dns_data},${cost}
done
echo dns_data: ${dns_data}
echo dns_delay: ${dns_delay}

# SID query
# sid_router=`dig +short sid.xuebing.name`
sid_router=`sudo ping sid.xuebing.name -w2|grep PING| head -n1| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
for i in `seq ${repeat}`
do
    output=`./server/client ${sid_router} ${sid_server}| grep cost| egrep -o '[0-9]+'`
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
