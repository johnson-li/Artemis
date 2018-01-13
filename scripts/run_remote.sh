#!/usr/bin/env bash

remote_ip=$1
sid_server=`sqlite3 ../resources/db/sip.db "select server from sip where host = '${remote_ip}'"`
#ssh goettingenple_txp1@${remote_ip} "for pid in `ps -ef|grep server| grep root| egrep -o ' [0-9]{2,} '`; do sudo kill -9 ${pid}; done"
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no goettingenple_txp1@${remote_ip} "./conduct_exp1.sh ${sid_server}"

