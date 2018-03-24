#!/bin/bash
cookie='Cookie:__utma=129731661.1387509532.1513851586.1513851586.1513851586.1; __utmz=129731661.1513851586.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=ltb9743lde1f85cgupfmvvu4l1; uechat_5038_first_time=1521918191191; uechat_5038_mode=0; uechat_5038_pages_count=9'
slice_id=1326
slice_name='goettingenple_txp1'

### data imported from config.sh
cookie=$cookie

response=`wget -qO- --header="$cookie" 'https://www.planet-lab.eu/db/nodes/index.php?active_line_tab=All+nodes'`
list=`echo "$response"|grep '/db/nodes/node.php?'|gawk 'match($0, /.*node\.php\?id=([0-9]+)'"'"'>([^<]+)<\/a><\/td><td class=.*node-k?ok?'"'"'>([^<]+)<.*/, value) { print value[1] " " value[2] " " value[3]}'`
echo "$list"
