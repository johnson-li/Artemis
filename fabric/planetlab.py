import json
import os
import re
import sys

import urllib2
from fabric.api import *

from hestia.tools.available_plt_hosts import HOSTS_FILE

reload(sys)
sys.setdefaultencoding("utf-8")

env.warn_only = True
env.skip_bad_hosts = True
env.use_ssh_config = True
env.ssh_config_path = os.path.dirname(os.path.dirname(__file__)) + '/resources/ssh/config_planetlab'

env.hosts = []

with open(HOSTS_FILE) as f:
    for line in f.readlines():
        env.hosts.append(line)


@parallel(pool_size=6)
def host_type():
    run('uname -a')


@parallel(pool_size=6)
def local_dns_latency():
    sudo(
        "ping -c 10 `sudo cat /etc/resolv.conf|grep nameserver|head -n1|egrep -o '[0-9.]+'`| tail -1| awk '{print $4}' | cut -d '/' -f 2")


@parallel(pool_size=6)
def install_quic_dependencies():
    sudo('yum install -y libnet-devel')


@parallel(pool_size=6)
def disk_size():
    run('df -h')


@parallel(pool_size=6)
def simple_client():
    run('./server/simple_client gcp.xuebing.name')


@parallel(pool_size=6)
def simple_client_repeat():
    run('./server/simple_client gcp.xuebing.name')
    run('./server/simple_client gcp.xuebing.name')
    run('./server/simple_client gcp.xuebing.name')


@parallel(pool_size=6)
def init():
    sudo('yum install -y gcc-c++ bind-utils')


@parallel(pool_size=6)
def test_dns_delay():
    sudo('dig miss.xuebing.name|grep Query')


@parallel(pool_size=10)
def trace_route():
    result = sudo('traceroute -n 8.8.8.8')
    fo = open("traceroute.csv", "a")
    fo.write(env.host)
    ip = ''
    location = ''
    asn = ''
    print(result)

    lines = result.split("\n")
    lines.reverse()
    for line in lines:
        s = re.search(r'\d+\.\d+\.\d+\.\d+', line)
        if s is not None:
            dns = s.group()
            url = 'http://ip-api.com/json/' + dns
            info = json.loads(urllib2.urlopen(url).read())
            if 'isp' in info and info['isp'] != 'Google':
                ip = dns
                location = info['city']
                asn = info['as']
                break
    fo.write(',' + ip + ',' + location + ',' + asn + '\n')
    fo.close()
    print(ip)
    print(location)


@parallel(pool_size=4)
def host():
    print(env.host)
