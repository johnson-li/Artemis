#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

target=35.227.98.160
root=/tmp/hestia/data
date > ${root}/start.sh.start_ts

# Useful values
timestamp=$(($(date +%s%N)/1000000))
client_ip=$(curl -s https://api.ipify.org)

# Install softwares
sudo apt update > /dev/null 2>&1
sudo apt install -y -qq dnsutils mysql-client libev-dev libmysqlclient-dev libmariadbclient18 > /dev/null 2>&1

latency_min=1000000
# Init database
while read line
do
    dc=hestia$(echo $line| cut -d' ' -f1| sed 's/-//g')
    dc_ip=$(echo $line| cut -d' ' -f2)
    server_ip=$(echo $line| cut -d' ' -f3)
    latency=$(ping -i.2 -c5 ${dc_ip} | tail -1| awk '{print $4}' | cut -d '/' -f 2)
    cmp=$(awk 'BEGIN{ print "'$latency'"<"'$latency_min'"  }')
    if [ $(bc <<< "$latency < $latency_min") -eq 1  ];then
        latency_min=latency
        target_server=$server_ip
        server_region=$dc
    fi
    mysql -h34.68.107.26 -ujohnson -pjohnson -Dserviceid_db -e "insert into measurements (dc, client, latency, ts) values ('${dc}', '${client_ip}', ${latency}, ${timestamp})"
done < ${root}/datacenters.txt

# Anycast probing
export router_region=`curl -s $lb_ip:110`
target=`python3 -c 'import os; import json; machines=json.load(open("/tmp/hestia/data/machine.json")); print(machines[os.environ["router_region"]]["external_ip2"])'`

# Conduct experiment with Hestia
echo sudo LD_LIBRARY_PATH=${root} ${root}/client ${target} 4433 2> ${root}/client_sid.log &
sudo LD_LIBRARY_PATH=${root} ${root}/client ${target} 4433 2> ${root}/client_sid.log &
pid=$!
sleep 5
sudo kill -9 ${pid}
transfer_time=`grep 'transfer time' /tmp/hestia/data/client_sid.log| cut -d' ' -f3`

# Conduct experiment with DNS
echo sudo LD_LIBRARY_PATH=${root} ${root}/client ${target_server} 4433 2> ${root}/client_dns.log &
sudo LD_LIBRARY_PATH=${root} ${root}/client ${target_server} 4433 2> ${root}/client_dns.log &
pid=$!
sleep 5
sudo kill -9 ${pid}
dns_transfer_time=`grep 'transfer time' /tmp/hestia/data/client_dns.log| cut -d' ' -f3`

dns_query_time=`dig xuebing.li|grep 'Query time'|cut -d' ' -f4`
hostname=`hostname`

if [ -z "$transfer_time" ]
then
    transfer_time=-1
fi
if [ -z "$dns_transfer_time" ]
then
    dns_transfer_time=-1
fi

sql="insert into transfer_time (client_ip, router_ip, server_ip, hostname, client_region, router_region, server_region, service_id_transfer_time, dns_query_time, dns_transfer_time, timestamp) values('${client_ip}', '${target}', '${target_server}', '${hostname}', '${region}', '${router_region}', '${server_region}', ${transfer_time}, ${dns_query_time}, ${dns_transfer_time}, ${timestamp});"
mysql -h34.68.107.26 -ujohnson -pjohnson -Dserviceid_db -e "${sql}"

date > ${root}/start.sh.end_ts
