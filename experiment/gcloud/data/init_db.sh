#!/bin/bash

date > ~/init_db.sh.start_ts

hostname=`hostname`
if [[ $hostname == *server  ]]
then
    date > ~/init_db.sh.end_ts
    exit 0
fi

if [[ $hostname == 'test' ]]
then
    sudo mysql -e "create database if not exists serviceid_db"
    sudo mysql -e "create user if not exists 'johnson' identified by 'johnson'"
    sudo mysql -e "GRANT USAGE ON *.* TO 'johnson'@'%' IDENTIFIED BY 'johnson'"
    sudo mysql -e "GRANT ALL privileges ON \`serviceid_db\`.* TO 'johnson'"
    sudo mysql -e "FLUSH PRIVILEGES"
    auth='-ujohnson -pjohnson'
elif [[ $hostname == *router  ]]
then
    echo root | unbuffer -p mysql_config_editor set --login-path=local --host=localhost --user=root --password --warn=false > /dev/null
    mysql --login-path=local -e "create database if not exists serviceid_db"
    mysql --login-path=local -e "create user if not exists 'johnson' identified by 'johnson'"
    mysql --login-path=local -e "GRANT USAGE ON *.* TO 'johnson'@'%' IDENTIFIED BY 'johnson'"
    mysql --login-path=local -e "GRANT ALL privileges ON \`serviceid_db\`.* TO 'johnson'"
    mysql --login-path=local -e "FLUSH PRIVILEGES"
    auth='--login-path=local'
    echo johnson | unbuffer -p mysql_config_editor set --login-path=local --host=localhost --user=johnson --password --warn=false > /dev/null
fi

if [[ $hostname == 'test' ]]
then
    mysql ${auth} -D serviceid_db -e "drop table if exists measurements"
    mysql ${auth} -D serviceid_db -e "drop table if exists deployment"
    mysql ${auth} -D serviceid_db -e "drop table if exists intra"
    mysql ${auth} -D serviceid_db -e "drop table if exists clients"

    mysql ${auth} -D serviceid_db -e "create table measurements (
        id int NOT NULL AUTO_INCREMENT,
        dc varchar(32),
        client varchar(32),
        latency int,
        ts int,
        primary key (id)
    )"
    mysql ${auth} -D serviceid_db -e "create table deployment (
        id int NOT NULL AUTO_INCREMENT,
        datacenter varchar(32),
        domain varchar(32),
        loadbalancer varchar(32),
        primary key (id),
        unique key (domain, datacenter)
    )"
    mysql ${auth} -D serviceid_db -e "create table intra (
        id int NOT NULL AUTO_INCREMENT,
        domain varchar(32),
        server varchar(32),
        datacenter varchar(32),
        sid varchar(32),
        weight int,
        primary key (id)
    )"
    mysql ${auth} -D serviceid_db -e "create table clients (
        id int NOT NULL AUTO_INCREMENT,
        ip varchar(32),
        primary key (id),
        unique key (ip)
    )"

    mysql ${auth} -D serviceid_db -e "insert into measurements (dc, client, latency, ts) values ('hestiauseast1c', '34.67.46.87', 10, 100);"
    mysql ${auth} -D serviceid_db -e "insert into measurements (dc, client, latency, ts) values ('hestiauseast4c', '34.67.46.87', 20, 100);"
    mysql ${auth} -D serviceid_db -e "insert into intra (domain, server, datacenter, sid, weight) values ('serviceid.xuebing.li', 'server', 'hestiauseast1c', '11.11.11.11', 1)"
    mysql ${auth} -D serviceid_db -e "insert into clients (ip) values ('34.67.46.87')"
    mysql ${auth} -D serviceid_db -e "insert into deployment (datacenter, domain, loadbalancer) values ('hestiauseast1c', 'serviceid.xuebing.li', 'bl0')"
fi


date > ~/init_db.sh.end_ts