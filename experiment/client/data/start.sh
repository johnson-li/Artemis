#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

mysql_ip=35.238.99.53
target=35.227.98.160
root=/tmp/hestia/data
date > ${root}/start.sh.start_ts

# Useful values
timestamp=$(($(date +%s%N)/1000000))
client_ip=$(curl -s https://api.ipify.org)

# Install softwares
sudo apt update > /dev/null 2>&1
sudo apt install -y -qq dnsutils bc mysql-client libev-dev libmysqlclient-dev libmariadbclient18

latency_min=1000000
# Init database
while read line
do
    dc=$(echo $line| cut -d' ' -f1)
    dc_ip=$(echo $line| cut -d' ' -f2)
    server_ip=$(echo $line| cut -d' ' -f3)
    latency=$(ping -i.2 -c5 ${dc_ip} | tail -1| awk '{print $4}' | cut -d '/' -f 2)
    cmp=$(awk 'BEGIN{ print "'$latency'"<"'$latency_min'"  }')
    if [[ $(bc <<< "$latency < $latency_min") -eq 1 ]];then
        latency_min=$latency
        target_server=$server_ip
        echo "min latency: $latency, from server: $server_ip, in region: $server_region"
    fi
    target_server=$server_ip
    server_region=`python3 -c "import os; print('-'.join([''.join((t[:2], t[-2:])) for t in '${dc}'.split('-')[:2]]))"`

    sql="insert into measurements (dc, client, latency, ts) values ('${server_region}', '${client_ip}', ${latency}, ${timestamp})"
    echo "sql: " $sql
    mysql -h${mysql_ip} -ujohnson -pjohnson -Dserviceid_db -e "${sql}"
done < ${root}/datacenters.txt

# Anycast probing
export router_region=`curl -s $lb_ip:110`
target=`python3 -c 'import os; import json; machines=json.load(open("/tmp/hestia/data/machine.json")); print(machines[os.environ["router_region"]]["external_ip2"])'`
target_anycast=`python3 -c 'import os; import json; machines=json.load(open("/tmp/hestia/data/machine.json")); print(machines[os.environ["router_region"][:-7] + "-server"]["external_ip1"])'`
echo "target: " $target

sleep 10
for i in `seq 5`
do
    # Conduct experiment with Hestia
    row_index=0
    row_total=$(cat ${root}/index.csv|wc -l)
    for row in $(cat ${root}/index.csv); do
        echo sudo LD_LIBRARY_PATH=${root} ${root}/client ${target} 4433 -i -w $row -q 2> ${root}/client_sid.log
        sudo LD_LIBRARY_PATH=${root} ${root}/client ${target} 4433 -i -w $row -q 2> ${root}/client_sid.log

        transfer_time=`grep -a 'transfer time' /tmp/hestia/data/client_sid.log| cut -d' ' -f3 | tail -n 1`
        handshake_time=`grep -a 'handshake time' /tmp/hestia/data/client_sid.log| cut -d' ' -f3 | tail -n 1`
        service_plt_time=`grep -a 'PLT: ' /tmp/hestia/data/client_sid.log| cut -d' ' -f2 | tail -n 1`

        #Conduct experiment with Anycast
        echo sudo LD_LIBRARY_PATH=${root} ${root}/client ${target_anycast} 4433 -i -w $row -q 2> ${root}/client_anycast.log
        sudo LD_LIBRARY_PATH=${root} ${root}/client ${target_anycast} 4433 -i -w $row -q 2> ${root}/client_anycast.log

        anycast_transfer_time=`grep -a 'transfer time' /tmp/hestia/data/client_anycast.log| cut -d' ' -f3 | tail -n 1`
        anycast_handshake_time=`grep -a 'handshake time' /tmp/hestia/data/client_anycast.log| cut -d' ' -f3 | tail -n 1`
        anycast_plt_time=`grep -a 'PLT: ' /tmp/hestia/data/client_anycast.log| cut -d' ' -f2 | tail -n 1`

        # Conduct experiment with DNS

        echo sudo LD_LIBRARY_PATH=${root} ${root}/client ${target_server} 4433 -i -w $row -q 2> ${root}/client_dns.log
        sudo LD_LIBRARY_PATH=${root} ${root}/client ${target_server} 4433 -i -w $row -q 2> ${root}/client_dns.log

        dns_transfer_time=`grep -a 'transfer time' /tmp/hestia/data/client_dns.log| cut -d' ' -f3 | tail -n 1`
        dns_handshake_time=`grep -a 'handshake time' /tmp/hestia/data/client_dns.log| cut -d' ' -f3 | tail -n 1`
        dns_plt_time=`grep -a 'PLT: ' /tmp/hestia/data/client_dns.log| cut -d' ' -f2 | tail -n 1`

        dns_query_time=`dig a.xuebing.li|grep 'Query time'|cut -d' ' -f4 | tail -n 1`
        hostname=`hostname`
        bind_server_ip=`grep -a 'bind fd2_ with' /tmp/hestia/data/client_sid.log| cut -d' ' -f4 | tail -n 1`


        if [ -z "$transfer_time" ]
        then
            transfer_time=-1
        fi
        if [ -z "$handshake_time" ]
        then
            handshake_time=-1
        fi
        if [ -z "$dns_transfer_time" ]
        then
            dns_transfer_time=-1
        fi
        if [ -z "$dns_handshake_time" ]
        then
            dns_handshake_time=-1
        fi
        if [ -z "$anycast_transfer_time" ]
        then
            anycast_transfer_time=-1
        fi
        if [ -z "$anycast_handshake_time" ]
        then
            anycast_handshake_time=-1
        fi
        if [ -z "$service_plt_time" ]
        then
            service_plt_time=-1
        fi
        if [ -z "$dns_plt_time" ]
        then
            dns_plt_time=-1
        fi
        if [ -z "$anycast_plt_time" ]
        then
            anycast_plt_time=-1
        fi
        if [ -z "$bind_server_ip" ]
        then
            bind_server_ip=-1
        fi
        if [ -z "$row" ]
        then
            row=-1
        fi

        sql="insert into transfer_time (client_ip, router_ip, server_ip, hostname, client_region, router_region, server_region, service_id_transfer_time, service_id_handshake_time, dns_query_time, dns_transfer_time, dns_handshake_time, anycast_transfer_time, anycast_handshake_time, service_plt_time, dns_plt_time, anycast_plt_time, bind_server_ip, website, timestamp) values('${client_ip}', '${target}', '${target_server}', '${hostname}', '${region}', '${router_region}', '${server_region}', ${transfer_time}, ${handshake_time}, ${dns_query_time}, ${dns_transfer_time},
        ${dns_handshake_time}, ${anycast_transfer_time}, ${anycast_handshake_time}, ${service_plt_time}, ${dns_plt_time}, ${anycast_plt_time},'${bind_server_ip}', '${row}', ${timestamp});"
        echo "sql: " $sql
        mysql -h${mysql_ip} -ujohnson -pjohnson -Dserviceid_db -e "${sql}"
    done
done

date > ${root}/start.sh.end_ts

