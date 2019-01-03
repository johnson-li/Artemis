create table deployment (
    id int NOT NULL AUTO_INCREMENT,
    datacenter varchar(255),
    domain varchar(255),
    primary key (id),
    unique key (domain, datacenter)
);