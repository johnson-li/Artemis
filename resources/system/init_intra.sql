create table intra (
    id int NOT NULL AUTO_INCREMENT,
    domain varchar(255),
    server varchar(255),
    sid varchar(255),
    weight int,
    primary key (id)
);
