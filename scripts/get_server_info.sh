#!/usr/bin/env bash

router_ip=`dig +short sid.xuebing.name`
dns_ip=`dig +short cdn2.xuebing.name`
region=`sqlite3 ../resources/db/instances.db "select region from instances where secondaryIpv4Pub = '${router_ip}'"`
server_ip=`sqlite3 ../resources/db/instances.db "select primaryIpv4Pub from instances where region = '${region}' and name = 'server'"`
echo SID pair: ${router_ip} ${server_ip}
echo DNS IP: ${dns_ip}
