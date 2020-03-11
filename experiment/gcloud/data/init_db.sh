#!/bin/bash

sudo mysql -e "create database if not exists serviceid_db"
sudo mysql -e "create user if not exists 'johnson' identified by 'johnson'"
sudo mysql -e "GRANT USAGE ON *.* TO 'johnson'@'%' IDENTIFIED BY 'johnson'"
sudo mysql -e "GRANT ALL privileges ON \`serviceid_db\`.* TO 'johnson'"
sudo mysql -e "FLUSH PRIVILEGES"

mysql -ujohnson -pjohnson -D serviceid_db -e "drop table if exists measurements"
mysql -ujohnson -pjohnson -D serviceid_db -e "drop table if exists deployment"
mysql -ujohnson -pjohnson -D serviceid_db -e "drop table if exists intra"
mysql -ujohnson -pjohnson -D serviceid_db -e "drop table if exists clients"

mysql -ujohnson -pjohnson -D serviceid_db -e "create table measurements (
    id int NOT NULL AUTO_INCREMENT,
    dc varchar(32),
    client varchar(32),
    latency int,
    ts int,
    primary key (id)
)"
mysql -ujohnson -pjohnson -D serviceid_db -e "create table deployment (
    id int NOT NULL AUTO_INCREMENT,
    datacenter varchar(32),
    domain varchar(32),
    loadbalancer varchar(32),
    primary key (id),
    unique key (domain, datacenter)
)"
mysql -ujohnson -pjohnson -D serviceid_db -e "create table intra (
    id int NOT NULL AUTO_INCREMENT,
    domain varchar(32),
    server varchar(32),
    datacenter varchar(32),
    sid varchar(32),
    weight int,
    primary key (id)
)"
mysql -ujohnson -pjohnson -D serviceid_db -e "create table clients (
    id int NOT NULL AUTO_INCREMENT,
    ip varchar(32),
    primary key (id),
    unique key (ip)
)"

mysql -ujohnson -pjohnson -D serviceid_db -e "insert into intra (domain, server, datacenter, sid, weight) values ('serviceid.xuebing.li', 'sv0', 'dc1', '11.11.11.11', 1)"
mysql -ujohnson -pjohnson -D serviceid_db -e "insert into clients (ip) values ('195.148.125.212')"
mysql -ujohnson -pjohnson -D serviceid_db -e "insert into deployment (datacenter, domain, loadbalancer) values ('dc1', 'serviceid.xuebing.li', 'bl0')"

