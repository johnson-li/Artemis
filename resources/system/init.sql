insert into intra (domain, server, datacenter, sid, weight) values ('site1.xuebingli.com', 'sv0', 'dc1', '173.16.156.100', 1);
insert into intra (domain, server, datacenter, sid, weight) values ('site1.xuebingli.com', 'sv1', 'dc1', '173.16.156.100', 2);
insert into intra (domain, server, datacenter, sid, weight) values ('site1.xuebingli.com', 'sv5', 'dc2', '174.16.156.100', 1);
insert into intra (domain, server, datacenter, sid, weight) values ('site1.xuebingli.com', 'sv6', 'dc2', '174.16.156.100', 2);

insert into clients (ip) values ('195.148.125.212');

insert into deployment (datacenter, domain, loadbalancer) values ('dc1', 'site1.xuebingli.com', 'bl0');
insert into deployment (datacenter, domain, loadbalancer) values ('dc2', 'site1.xuebingli.com', 'bl5');

insert into measurements (dc, client, latency, ts) values ('dc1', '170.16.156.1', 10, 100);
insert into measurements (dc, client, latency, ts) values ('dc2', '170.16.156.1', 1, 100);
insert into measurements (dc, client, latency, ts) values ('dc1', '171.16.156.1', 10, 100);
insert into measurements (dc, client, latency, ts) values ('dc2', '171.16.156.1', 100, 100);
insert into measurements (dc, client, latency, ts) values ('dc1', '173.16.156.1', 10, 100);
--insert into measurements (dc, client, latency, ts) values ('dc2', '173.16.156.1', 100, 100);
insert into measurements (dc, client, latency, ts) values ('dc2', '173.16.156.1', 1, 100);
insert into measurements (dc, client, latency, ts) values ('dc1', '174.16.156.1', 10, 100);
insert into measurements (dc, client, latency, ts) values ('dc2', '174.16.156.1', 100, 100);
