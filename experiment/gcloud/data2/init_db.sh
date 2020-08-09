#!/bin/bash

date > ~/init_db.sh.start_ts

test_server_ip="35.238.34.228"
hostname=$(hostname)
if [[ $hostname == *server  ]]
then
    date > ~/init_db.sh.end_ts
    exit 0
fi

if [[ $hostname == 'workstation' ]]
then
    sudo mysql -e "create database if not exists serviceid_db" > /dev/null
    sudo mysql -e "create user if not exists 'johnson' identified by 'johnson'" > /dev/null
    sudo mysql -e "GRANT USAGE ON *.* TO 'johnson'@'%' IDENTIFIED BY 'johnson'" > /dev/null
    sudo mysql -e "GRANT ALL privileges ON \`serviceid_db\`.* TO 'johnson'" > /dev/null
    sudo mysql -e "FLUSH PRIVILEGES" > /dev/null
    auth='-ujohnson -pjohnson'
    #auth='--login-path=local'
    #echo johnson | unbuffer -p mysql_config_editor set --login-path=local --host=localhost --user=johnson --password --warn=false > /dev/null
else
    echo root | unbuffer -p mysql_config_editor set --login-path=local --host=localhost --user=root --password --warn=false > /dev/null
    mysql --login-path=local -e "create database if not exists serviceid_db" > /dev/null
    mysql --login-path=local -e "create user if not exists 'johnson' identified by 'johnson'" > /dev/null
    mysql --login-path=local -e "GRANT USAGE ON *.* TO 'johnson'@'%' IDENTIFIED BY 'johnson'" > /dev/null
    mysql --login-path=local -e "GRANT ALL privileges ON \`serviceid_db\`.* TO 'johnson'" > /dev/null
    mysql --login-path=local -e "FLUSH PRIVILEGES" > /dev/null
    auth='--login-path=local'
    echo johnson | unbuffer -p mysql_config_editor set --login-path=local --host=localhost --user=johnson --password --warn=false > /dev/null
fi

if [[ $hostname == 'workstation' ]]
then
    mysql ${auth} -D serviceid_db -e "drop table if exists measurements" 2> /dev/null
    mysql ${auth} -D serviceid_db -e "drop table if exists deployment" 2> /dev/null
    mysql ${auth} -D serviceid_db -e "drop table if exists intra" 2> /dev/null
    mysql ${auth} -D serviceid_db -e "drop table if exists clients" 2> /dev/null
    mysql ${auth} -D serviceid_db -e "drop table if exists transfer_time" 2> /dev/null

    mysql ${auth} -D serviceid_db -e "create table measurements (
        id int NOT NULL AUTO_INCREMENT,
        dc varchar(32),
        client varchar(32),
        latency FLOAT,
        ts BIGINT,
        primary key (id)
    )" 2> /dev/null
    mysql ${auth} -D serviceid_db -e "create table deployment (
        id int NOT NULL AUTO_INCREMENT,
        datacenter varchar(32),
        domain varchar(32),
        loadbalancer varchar(32),
        primary key (id),
        unique key (domain, datacenter)
    )" 2> /dev/null
    mysql ${auth} -D serviceid_db -e "create table intra (
        id int NOT NULL AUTO_INCREMENT,
        domain varchar(32),
        server varchar(32),
        datacenter varchar(32),
        sid varchar(32),
        weight int,
        primary key (id)
    )" 2> /dev/null
    mysql ${auth} -D serviceid_db -e "create table clients (
        id int NOT NULL AUTO_INCREMENT,
        ip varchar(32),
        primary key (id),
        unique key (ip)
    )" 2> /dev/null
    mysql ${auth} -D serviceid_db -e "create table transfer_time (
        id int NOT NULL AUTO_INCREMENT,
        client_ip varchar(32),
        router_ip varchar(32),
        server_ip varchar(32),
        hostname varchar(1024),
        client_region varchar(1024),
        router_region varchar(1024),
        server_region varchar(1024),
        service_id_transfer_time integer,
        service_id_handshake_time integer,
        dns_query_time integer,
        dns_transfer_time integer,
        dns_handshake_time integer,
        anycast_transfer_time integer,
        anycast_handshake_time integer,
        service_plt_time integer,
        dns_plt_time integer,
        anycast_plt_time integer,
        bind_server_ip varchar(32),
        website varchar(32),
        timestamp bigint,
        primary key (id)
    )" 2> /dev/null

    declare -a arr=("usus-eat1" "usus-eat4" "usus-cel1" "usus-wet1" "usus-wet2" "usus-wet3" "eupe-wet1" "eupe-wet2" "eupe-wet3" "eupe-wet4" "eupe-wet6" "eupe-noh1" "asia-eat1" "asia-eat2" "asia-sot1" "asia-not1" "asia-not2" "asia-not3" "asia-soh1" "auia-sot1" "soca-eat1" "noca-not1")
    for zone in "${arr[@]}"
    do
        mysql ${auth} -D serviceid_db -e "insert into intra (domain, server, datacenter, sid, weight) values ('serviceid.xuebing.li', 'server', '${zone}', '11.11.11.11', 1)" 2> /dev/null
        mysql ${auth} -D serviceid_db -e "insert into deployment (datacenter, domain, loadbalancer) values ('${zone}', 'serviceid.xuebing.li', '${zone}')" 2> /dev/null
    done
    #mysql ${auth} -D serviceid_db -e "insert into deployment (datacenter, domain, loadbalancer) values ('uscentral1c', 'serviceid.xuebing.li', 'uscentral1c')" 2> /dev/null
fi


date > ~/init_db.sh.end_ts
