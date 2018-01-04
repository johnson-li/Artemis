#!/usr/bin/env bash

remote_ip=$1
sid_server=`sqlite3 ../resources/db/sip.db "select server from sip where host = '${remote_ip}'"`
ssh goettingenple_txp1@${remote_ip} "./conduct_exp1.sh ${sid_server}"

