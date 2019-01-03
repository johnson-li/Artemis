create table measurements (
    id int NOT NULL AUTO_INCREMENT,
    dc varchar(255),
    client varchar(255),
    latency int,
    ts int,
    primary key (id)
)