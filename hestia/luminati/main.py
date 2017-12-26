#!/usr/bin/env python
import urllib.request

opener = urllib.request.build_opener(
    urllib.request.ProxyHandler(
        {'http': 'http://lum-customer-hl_303467b7-zone-static:1vxwft304ba9@zproxy.luminati.io:22225'}))
print(opener.open('http://lumtest.com/myip.json').read())
