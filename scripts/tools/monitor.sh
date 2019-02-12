#!/usr/bin/env bash

mkdir -p data

programme="$1"

pid=`pidof ${programme}`

ts=`echo $(($(date +%s%N)/1000000))`

sudo pmap ${pid}

memory=`sudo pmap ${pid}| tail -n1| egrep -o '[0-9]+'`

echo ${memory} >> "data/${programme}-${ts}"
