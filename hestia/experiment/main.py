import argparse
import json
import os
import re
import socket
import sqlite3
import sys
from http.client import HTTPConnection
from multiprocessing.pool import ThreadPool

import paramiko

from hestia import RESOURCE_PATH, SQL_PATH
from hestia.aws.regions import REGIONS
from hestia.info.dpid import DPID
from hestia.info.mac import MAC
from hestia.gce.zones import shrink

DB_PATH = RESOURCE_PATH + '/db'
DB_FILE = DB_PATH + '/sip.db'
INSTANCE_DB_FILE = DB_PATH + '/instances.db'
SQL_FILE = SQL_PATH + '/sip.sql'
ssh_clients = {}
host_mapping = {}
PLATFORM = 'AWS'


def init_db():
    if not os.path.exists(DB_PATH):
        os.mkdir(DB_PATH)
    if not os.path.exists(DB_FILE):
        print('Init DB')
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        init_sql = ''.join(open(SQL_FILE).readlines())
        c.execute(init_sql)
        c.close()
        conn.close()


def store_result(host, server):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("select * from sip where host = '{}'".format(host))
    if c.fetchone():
        c.execute("UPDATE sip set server = '{}' where host = '{}'".format(server, host))
    else:
        c.execute("insert into sip (host, server) VALUES ('{}', '{}')".format(host, server))
    conn.commit()
    c.close()
    conn.close()


def get_ssh(host):
    if host in ssh_clients.keys():
        return ssh_clients[host]
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_config = paramiko.SSHConfig()
    with open(RESOURCE_PATH + '/ssh/config') as f:
        ssh_config.parse(f)
    cfg = ssh_config.lookup(host)
    ssh.connect(cfg['hostname'], username=cfg['user'], key_filename=cfg['identityfile'])
    host_mapping[host] = cfg['hostname']
    ssh_clients[host] = ssh
    return ssh


def get_latency(region, peer):
    host = region + '-server'
    ssh = get_ssh(host)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
        "ping -c 10 " + peer + " | tail -1| awk '{print $4}' | cut -d '/' -f 2")
    for line in ssh_stdout:
        return region, float(line)


def get_port(host, port_name):
    ssh = get_ssh(host)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sudo ovs-ofctl show br1| grep '({})'".format(port_name))
    for line in ssh_stdout:
        return re.search('[0-9]+', line).group()


class StaticFlowPusher(object):

    def __init__(self, server):
        self.server = server

    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])

    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200

    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200

    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }
        body = json.dumps(data)
        conn = HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        conn.close()
        return ret


pusher = StaticFlowPusher('35.193.107.149')


def add_default_flow(region):
    # router -> server
    flow = {
        'switch': DPID[region]['router'],
        'name': '{}-route-server-default'.format(region),
        'cookie': '0',
        'eth_type': '0x0800',
        'priority': '10',
        'in_port': get_port(region + '-router', 'eth1' if PLATFORM == 'AWS' else 'ens5'),
        'active': 'true',
        'actions': 'output={}'.format(get_port(region + '-router', 'gre_server')),
    }
    print(flow)
    pusher.set(flow)
    # server -> local
    flow = {
        'switch': DPID[region]['server'],
        'name': '{}-server-default'.format(region),
        'cookie': '0',
        'eth_type': '0x0800',
        'priority': '200',
        'in_port': get_port(region + '-server', 'gre_router'),
        'active': 'true',
        'actions': 'set_field=ipv4_dst->10.10.10.10,set_field=eth_dst->{},output=local'.format(
            MAC[region]['server']['br1']),
    }
    print(flow)
    pusher.set(flow)


def add_default_flows(all_regions):
    pool.map(add_default_flow, all_regions)


def add_route_flow(target, other_region, peer_ip):
    flow = {
        'switch': DPID[other_region]['router'],
        'name': 'route-{}-{}'.format(other_region, peer_ip),
        'cookie': '0',
        'eth_type': '0x0800',
        'ipv4_src': peer_ip,
        'priority': '100',
        'in_port': get_port(other_region + '-router', 'eth1' if PLATFORM == 'AWS' else 'ens5'),
        'active': 'true',
        'actions': 'output={}'.format(get_port(other_region + '-router', 'gre_' + shrink(target))),
    }
    pusher.set(flow)
    print(flow)


def add_flows(target, other_regions, peer_ip):
    # router -> router forwarding
    pairs = [(target, other_region, peer_ip) for other_region in other_regions]
    pool.starmap(add_route_flow, pairs)

    # router(eth) -> server forwarding
    flow = {
        'switch': DPID[target]['router'],
        'name': 'route-{}-{}'.format(target, peer_ip),
        'cookie': '0',
        'eth_type': '0x0800',
        'ipv4_src': peer_ip,
        'priority': '200',
        # 'in_port': get_port(target + '-router', 'eth1' if PLATFORM == 'AWS' else 'ens5'),
        'active': 'true',
        'actions': 'output={}'.format(get_port(target + '-router', 'gre_server')),
    }
    print(flow)
    pusher.set(flow)

    # router(gre) -> server forwarding
    flow = {
        'switch': DPID[target]['router'],
        'name': 'route-{}'.format(peer_ip),
        'cookie': '0',
        'eth_type': '0x0800',
        'ipv4_src': peer_ip,
        'priority': '100',
        'in_port': get_port(target + '-router', 'eth1' if PLATFORM == 'AWS' else 'ens5'),
        'active': 'true',
        'actions': 'output={}'.format(get_port(target + '-router', 'gre_server')),
    }
    print(flow)
    pusher.set(flow)


peer = '35.193.107.149'
concurrency = 8
pool = ThreadPool(8)

if __name__ == '__main__':
    global PLATFORM
    global DB_FILE
    global INSTANCE_DB_FILE
    parser = argparse.ArgumentParser(description='Setup gre bridges between hosts.')
    parser.add_argument('--platform', dest='platform', type=str, default='AWS', choices=['AWS', 'GCP'],
                        help='the cloud platform, GCP or AWS')
    args = parser.parse_args()
    PLATFORM = args.platform
    if PLATFORM == 'GCP':
        INSTANCE_DB_FILE = DB_PATH + '/gcp_instances.db'

    conn = sqlite3.connect(INSTANCE_DB_FILE)
    c = conn.cursor()
    c.execute("SELECT region FROM instances GROUP BY region")
    regions = []
    for region in c.fetchall():
        region = region[0]
        regions.append(REGIONS[region].lower() if PLATFORM == 'AWS' else region)
    if len(sys.argv) == 2:
        peer = sys.argv[1]
    else:
        add_default_flows(regions)
    peer = socket.gethostbyname(peer)
    init_db()
    results = []
    pairs = [(region, peer) for region in regions]
    results = pool.starmap(get_latency, pairs)
    results.sort(key=lambda pair: pair[1])
    # results = [('tokyo', 126.537), ('sydney', 173.48), ('singapore', 189.041)]
    print(results)
    store_result(peer, host_mapping[results[0][0] + '-server'])
    add_flows(results[0][0], [i[0] for i in results[1:]], peer)
