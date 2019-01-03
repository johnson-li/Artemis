create table clients (
    id int NOT NULL AUTO_INCREMENT,
    ip varchar(255),
    primary key (id),
    unique key (ip)
);