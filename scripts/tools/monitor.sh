#!/usr/bin/env bash

mkdir -p data

programme="$1"

pid=`pidof ${programme}`

ts=`echo $(($(date +%s%N)/1000000))`

memory=`sudo pmap ${pid}| tail -n1| egrep -o '[0-9]+'`

echo "${ts} ${memory}" >> "data/${programme}-memory"

