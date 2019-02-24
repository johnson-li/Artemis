#!/usr/bin/env bash

mkdir -p data
rm data/*

programme="$1"


while true
do
    pid=`pidof ${programme}`
    ts=`echo $(($(date +%s%N)/1000000))`
    memory=`sudo pmap ${pid}| tail -n1| egrep -o '[0-9]+'`
    cpu=`ps -eo pcpu,args -q ${pid}| tail -n1 | cut -d' ' -f2`
    echo "${ts} ${memory}" >> "data/${programme}-memory"
    echo "${ts} ${cpu}" >> "data/${programme}-cpu"
done

ps -eo pcpu,args -q `pidof client`| tail -n1 | cut -d' ' -f2