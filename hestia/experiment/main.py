import argparse
import json
import os
import re
import socket
import sqlite3
from http.client import HTTPConnection
from multiprocessing.pool import ThreadPool

import paramiko

from hestia import RESOURCE_PATH, SQL_PATH
from hestia.aws.regions import REGIONS, REVERSE_REGIONS
from hestia.gce.zones import shrink
from hestia.info.dpid import DPID
from hestia.info.mac import MAC

DB_PATH = RESOURCE_PATH + '/db'
DB_FILE = DB_PATH + '/sip.db'
INSTANCE_DB_FILE = DB_PATH + '/instances.db'
SQL_FILE = SQL_PATH + '/sip.sql'
ssh_clients = {}
host_mapping = {}
PLATFORM = 'AWS'


def is_aws():
    return PLATFORM == 'AWS'


def get_region(region):
    if is_aws():
        return REGIONS[region].lower()
    return region


def init_db():
    if not os.path.exists(DB_PATH):
        os.mkdir(DB_PATH)
    if not os.path.exists(DB_FILE):
        print('Init DB')
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        init_sql = ''.join(open(SQL_FILE).readlines())
        c.execute(init_sql)
        conn.commit()
        c.close()
        conn.close()


def get_router_secondary_ipv4(region, pub=False):
    conn = sqlite3.connect(INSTANCE_DB_FILE)
    c = conn.cursor()
    c.execute(
        "select secondaryIpv4{} from instances where name = 'router' and region = '{}'".format('Pub' if pub else '',
                                                                                               region))
    res = c.fetchone()[0]
    conn.close()
    return res


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
    region = get_region(region)
    host = region + '-server'
    ssh = get_ssh(host)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
        "ping -c 10 " + peer + " | tail -1| awk '{print $4}' | cut -d '/' -f 2")
    for line in ssh_stdout:
        return region, float(line)


def get_port(host, port_name):
    if port_name == 'br1':
        return 'local'
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
    region_name = region
    region = get_region(region)
    # router -> server
    flow = {
        'switch': DPID[region]['router'],
        'name': '{}-route-server-default'.format(region),
        'cookie': '0',
        'eth_type': '0x0800',
        'priority': '10',
        'in_port': get_port(region + '-router', 'eth1' if is_aws() else 'ens5'),
        'active': 'true',
        'actions': 'output={}'.format(get_port(region + '-router', 'gre_server')),
    }
    print(flow)
    pusher.set(flow)
    # router -> internet
    flow = {
        'switch': DPID[region]['router'],
        'name': '{}-route-internet'.format(region),
        'cookie': '0',
        'eth_type': '0x0800',
        'priority': '10',
        'in_port': get_port(region + '-router', 'gre_server'),
        'active': 'true',
        'actions': 'set_field=ipv4_src->{},set_field=eth_src->{},output={}'.format(
            get_router_secondary_ipv4(region_name), MAC[region]['router']['eth1' if is_aws() else 'ens5'],
            get_port(region + '-router', 'eth1' if is_aws() else 'ens5')),
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
    # server -> router
    flow = {
        'switch': DPID[region]['server'],
        'name': '{}-server-router'.format(region),
        'cookie': '0',
        'eth_type': '0x0800',
        'priority': '200',
        'in_port': get_port(region + '-server', 'br1'),
        'active': 'true',
        'actions': 'output={}'.format(get_port(region + '-server', 'gre_router')),
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
        'ip_proto': '0x11',
        'ipv4_src': peer_ip,
        'udp_dst': '8081',
        'priority': '100',
        'in_port': get_port(other_region + '-router', 'eth1' if is_aws() else 'ens5'),
        'active': 'true',
        'actions': 'output={}'.format(get_port(other_region + '-router', shrink(target))),
    }
    pusher.set(flow)
    print(flow)


def set_arp(target, peer_ip):
    print('Set arp for %s in %s' % (peer_ip, target))
    ssh_server = get_ssh(target + '-server')
    ssh_router = get_ssh(target + '-router')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_router.exec_command("cat ~/neigh.mac")
    for line in ssh_stdout:
        mac = line.strip()
        break
    ssh_server.exec_command("sudo arp -s %s %s -i br1" % (peer_ip, mac))


def add_flows(target, other_regions, peer_ip):
    pairs = [(region, peer_ip) for region in other_regions]
    pairs.append((target, peer_ip))
    pool.starmap(set_arp, pairs)

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
        # 'in_port': get_port(target + '-router', 'eth1' if is_aws() else 'ens5'),
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
        'in_port': get_port(target + '-router', 'eth1' if is_aws() else 'ens5'),
        'active': 'true',
        'actions': 'output={}'.format(get_port(target + '-router', 'gre_server')),
    }
    print(flow)
    pusher.set(flow)


DEFAULT_PEER = '35.193.107.149'
concurrency = 8
pool = ThreadPool(8)


def run(peer):
    conn = sqlite3.connect(INSTANCE_DB_FILE)
    c = conn.cursor()
    c.execute("SELECT region FROM instances GROUP BY region")
    regions = []
    for region in c.fetchall():
        region = region[0]
        regions.append(region)
    if peer == DEFAULT_PEER:
        add_default_flows(regions)
    peer = socket.gethostbyname(peer)
    results = []
    pairs = [(region, peer) for region in regions]
    results = pool.starmap(get_latency, pairs)
    results.sort(key=lambda pair: pair[1])
    # results = [('tokyo', 126.537), ('sydney', 173.48), ('singapore', 189.041)]
    print(results)
    get_ssh(results[0][0] + '-router')
    store_result(peer, get_router_secondary_ipv4(REVERSE_REGIONS[results[0][0]], pub=True))
    add_flows(results[0][0], [i[0] for i in results[1:]], peer)


def init(clear_db=False):
    global INSTANCE_DB_FILE
    if PLATFORM == 'GCP':
        INSTANCE_DB_FILE = DB_PATH + '/gcp_instances.db'
    if clear_db:
        os.remove(DB_FILE)
    init_db()


def main():
    global PLATFORM
    parser = argparse.ArgumentParser(description='Setup gre bridges between hosts.')
    parser.add_argument('--platform', dest='platform', type=str, default='AWS', choices=['AWS', 'GCP'],
                        help='the cloud platform, GCP or AWS')
    parser.add_argument('--peer', default=DEFAULT_PEER, help='the IP of the client')
    args = parser.parse_args()
    peer = args.peer
    PLATFORM = args.platform
    init(peer == DEFAULT_PEER)
    run(peer)


if __name__ == '__main__':
    main()
