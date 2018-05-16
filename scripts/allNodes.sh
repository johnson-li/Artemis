#!/bin/bash
cookie='Cookie:__utma=129731661.1387509532.1513851586.1513851586.1513851586.1; __utmz=129731661.1513851586.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=ltb9743lde1f85cgupfmvvu4l1; uechat_5038_first_time=1521918191191; uechat_5038_mode=0; uechat_5038_pages_count=9'
cookie='Cookie:PHPSESSID=26jimllj4gtq9m2cad519fsi36; uechat_5038_first_time=1526454395051; uechat_5038_mode=0; uechat_5038_pages_count=3'
slice_id=1326
slice_name='goettingenple_txp1'

response=`wget -qO- --header="$cookie" 'https://www.planet-lab.eu/db/nodes/index.php?active_line_tab=All+nodes'`
list=`echo "$response"|grep '/db/nodes/node.php?'|gawk 'match($0, /.*node\.php\?id=([0-9]+)'"'"'>([^<]+)<\/a><\/td><td class=.*node-k?ok?'"'"'>([^<]+)<.*/, value) { print value[1] " " value[2] " " value[3]}'`
echo "$list"
