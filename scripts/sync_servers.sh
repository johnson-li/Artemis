#!/usr/bin/env bash

for host in `grep '\-router' ../resources/ssh/config| cut -d' ' -f2`
do
    echo sync ${host}
    ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -F ../resources/ssh/config ${host} 'mkdir ~/Workspace/server'
    scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -F ../resources/ssh/config ../udp-server/client ${host}:~/Workspace/server/
    scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -F ../resources/ssh/config ../udp-server/dns_server ${host}:~/Workspace/server/
    scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -F ../resources/ssh/config ../udp-server/serviceid_server ${host}:~/Workspace/server/
done
