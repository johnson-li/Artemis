#!/usr/bin/env bash

if [ -z ${repeat+x} ]
then
    repeat=10
fi
echo repeat: ${repeat}

for i in `seq ${repeat}`
do
    output=`./server/simple_client cdn${i}.xuebing.name`
    cost=`echo "${output}"| grep cost| egrep -o '[0-9.]+'`
    dns_cost=`echo "${output}"| grep 'DNS delay'| egrep -o '[0-9.]+'`
    dns_delay=${dns_delay},${dns_cost}
    dns_server=`echo "${output}"| grep 'server ip by DNS'| egrep -o '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'`
    dns_servers=${dns_servers},${dns_server}
    if [ -z "$cost" ]
    then
        cost=0
    fi
    dns_data=${dns_data},${cost}
done
echo dns_servers: ${dns_servers}
echo dns_data: ${dns_data}
echo dns_delay: ${dns_delay}
