#!/usr/bin/env bash

old_dir=`pwd`
cd "$(dirname "$0")"/..
docker rm `docker ps -aq`
docker rmi `docker images -f dangling=true -q`
docker network create --subnet=172.18.0.0/16 hestianet
docker build --no-cache -t hestia:v1 -f dockerfiles/Dockerfile .
docker run --net hestianet --ip 172.18.0.100 --env-file dockerfiles/router.env --name router1 hestia:v1
docker run --net hestianet --ip 172.18.0.101 --env-file dockerfiles/server.env --name server1 hestia:v1

cd ${old_dir}



