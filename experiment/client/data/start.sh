BASEDIR=$(dirname "$0")

target=35.227.98.160
root=/tmp/hestia/data
date > ${root}/start.sh.start_ts

# Useful values
timestamp=$(($(date +%s%N)/1000000))
client_ip=$(curl -s https://api.ipify.org)

# Install softwares
sudo apt install -y -qq dnsutils mysql-client libev-dev libmysqlclient-dev libmariadbclient18 > /dev/null 2>&1

# Init database
while read line
do
    dc=hestia$(echo $line| cut -d' ' -f1| sed 's/-//g')
    dc_ip=$(echo $line| cut -d' ' -f2)
    latency=$(ping -i.2 -c5 ${dc_ip} | tail -1| awk '{print $4}' | cut -d '/' -f 2)
    mysql -h34.68.107.26 -ujohnson -pjohnson -Dserviceid_db -e "insert into measurements (dc, client, latency, ts) values ('${dc}', '${client_ip}', ${latency}, ${timestamp})"
done < ${root}/datacenters.txt

# Simulate anycast routing
#lb_list=$(gcloud compute addresses list)
#lb_list=${lb_list#*ipv4}
#lb_list=${lb_list%%EX*}
#lb_ip=`echo $lb_list | sed 's/ //g'`
export target_instance=`curl -s $lb_ip:110`
target=`python3 -c 'import os; import json; machines=json.load(open("/tmp/hestia/data/machine.json")); print(machines[os.environ["target_instance"]]["external_ip2"])'`

# Conduct experiment
echo sudo LD_LIBRARY_PATH=${root} ${root}/client ${target} 4433 2> ${root}/client.log &
sudo LD_LIBRARY_PATH=${root} ${root}/client ${target} 4433 2> ${root}/client.log &
pid=$!
sleep 3
sudo kill -9 ${pid}
transfer_time=`grep 'transfer time' /tmp/hestia/data/client.log| cut -d' ' -f3`

dns_query_time=`dig xuebing.li|grep 'Query time'|cut -d' ' -f4`
dns_transfer_time=0
hostname=`hostname`

if [ -z "$transfer_time" ]
then
    transfer_time=-1
fi

sql="insert into transfer_time (client_ip, target_ip, hostname, region, service_id_transfer_time, dns_query_time, dns_transfer_time, timestamp) values('${client_ip}', '${target}', '${hostname}', '${region}', ${transfer_time}, ${dns_query_time}, ${dns_transfer_time}, ${timestamp});"
mysql -h34.68.107.26 -ujohnson -pjohnson -Dserviceid_db -e "${sql}"

date > ${root}/start.sh.end_ts
