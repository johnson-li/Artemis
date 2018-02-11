#!/usr/bin/env bash
gcc dns_server.c -o dns_server
gcc serviceid_server.c -o serviceid_server
gcc client.c -o client
gcc simple_client.c -o simple_client
gcc -m32 client.c -o i686/client
gcc -m32 simple_client.c -o i686/simple_client

