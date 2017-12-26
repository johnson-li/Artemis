create table instances (
    id integer primary key,
    region varchar(255),
    name varchar(255),
    instanceId varchar(255),
    primaryIpv4 varchar(255),
    primaryIpv4Pub varchar(255),
    primaryIpv6 varchar(255),
    secondaryIpv4 varchar(255),
    secondaryIpv6 varchar(255),
    constraint chk_name check (name in ('server', 'router', 'None'))
);