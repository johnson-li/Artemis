#!/usr/bin/env bash

for host in `grep '\-router' ../resources/ssh/config| cut -d' ' -f2`
do
    echo sync ${host}
    ssh -F ../resources/ssh/config 'mkdir ~/Workspace/server'
    scp -F ../resources/ssh/config ../udp-server/client ${host}:~/Workspace/server/
    scp -F ../resources/ssh/config ../udp-server/dns_server ${host}:~/Workspace/server/
    scp -F ../resources/ssh/config ../udp-server/serviceid_server ${host}:~/Workspace/server/
done
