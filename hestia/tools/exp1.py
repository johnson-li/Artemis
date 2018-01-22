import json
import re
import sqlite3
from pprint import pprint

import matplotlib.pyplot as plt
import numpy

from hestia.aws.regions import REGIONS

PATH = '/Users/johnson/exp1/full'
INSTANCES_DB = '/Users/johnson/exp1/full/instances.db'
SIP_DB = '/Users/johnson/exp1/full/sip.db'


def parse_local_dns_latency():
    res = {}
    file = PATH + '/' + 'local_dns_latency'
    with open(file) as f:
        for line in f.readlines():
            match = re.match('\[(.+)\] out: ([0-9.]+)', line[:-1])
            if match:
                host = match.group(1)
                delay = match.group(2)
                res[host] = {'latency': float(delay)}
    return res


def parse():
    records = {}
    for file in ['exp1', 'exp1_32', 'exp1_32_last_10-19', 'exp1_32_last_20-29', 'exp1_32_last_30-39',
                 'exp1_32_last_40-49', 'exp1_32_last_50-59']:
        # for file in ['exp1']:
        file = PATH + '/' + file
        with open(file) as f:
            for line in f.readlines():
                if line.startswith('host: '):
                    host = line[6:-1]
                    record = {}
                elif line.startswith('direct_data'):
                    direct_data = line[14:-1]
                    record['direct_data'] = [float(i) for i in direct_data.split(',')]
                elif line.startswith('dns_hit_data'):
                    dns_hit_data = line[15:-1]
                    record['dns_hit_data'] = [float(i) if i else 0 for i in dns_hit_data.split(',')]
                elif line.startswith('dns_hit_delay'):
                    dns_hit_delay = line[16:-1]
                    record['dns_hit_delay'] = [float(i) if i else 0 for i in dns_hit_delay.split(',')]
                elif line.startswith('dns_data'):
                    dns_data = line[11:-1]
                    record['dns_data'] = [float(i) for i in dns_data.split(',')]
                elif line.startswith('dns_delay'):
                    dns_delay = line[12:-1]
                    record['dns_delay'] = [float(i) if i else 0 for i in dns_delay.split(',')]
                elif line.startswith('sid_data'):
                    sid_data = line[11:-1]
                    record['sid_data'] = [float(i) for i in sid_data.split(',')]
                elif line.startswith('direct_server'):
                    record['direct_server'] = line[15:-1]
                elif line.startswith('dns_servers'):
                    dns_servers = line[14:-1]
                    record['dns_servers'] = dns_servers.split(',')
                elif line.startswith('sid_router'):
                    record['sid_router'] = line[12:-1]
                elif line.startswith('sid_server'):
                    record['sid_server'] = line[12:-1]
                    records[host] = record
                elif line.startswith('['):
                    record['ping'] = dict(eval(line[:-1]))
    return records


def transform(records):
    records = {
        key: [{val_key: val[val_key][i] if isinstance(val[val_key], list) else val[val_key] for val_key in
               ['direct_data', 'dns_hit_data', 'dns_hit_delay', 'dns_data', 'dns_delay', 'sid_data', 'direct_server',
                'dns_servers', 'sid_router', 'sid_server']} for
              i in range(20)] for key, val in records.items()}
    for key in records.keys():
        records[key] = list(filter(lambda x: all(i != 0 for i in x.values()), records[key]))
    records = {key: val for key, val in records.items() if val}
    return records


def records_percentile(records, percentile):
    res = {}
    for key in records.keys():
        record = records[key]
        median = {}
        for data_key in record[0].keys():
            if isinstance(record[0][data_key], float):
                data = [record[i][data_key] for i in range(len(record))]
                median[data_key] = numpy.percentile(data, percentile)
        median['hit_increment'] = median['dns_hit_data'] - median['direct_data']
        median['sid_increment'] = median['sid_data'] - median['direct_data']
        median['sid_hit_incr'] = median['sid_data'] - median['dns_hit_data']
        res[key] = median
    return res


def plot(fig, records, key):
    data = [d[key] for d in records.values()]
    data = sorted(data)
    print({key: {a: b[key] for a, b in records.items()}})
    p = 1. * numpy.arange(len(data)) / (len(data) - 1)
    ax1 = fig.add_subplot(121)
    ax1.plot(data, p, label=key)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('CDF')
    ax1.legend(loc="lower right")


def compare(records):
    records = transform(records)
    records_median = records_percentile(records, 50)
    pprint(records_median)
    # print(records_median)
    fig = plt.figure(figsize=(8, 6), dpi=320)
    # plot(fig, records_median, 'direct_data')
    # plot(fig, records_median, 'dns_hit_data')
    # plot(fig, records_median, 'dns_data')
    # plot(fig, records_median, 'sid_data')
    # plot(fig, records_median, 'dns_delay')
    # plot(fig, records_median, 'hit_increment')
    # plot(fig, latency_map, 'latency')
    # plot(fig, records_median, 'sid_increment')
    plot(fig, records_median, 'sid_hit_incr')
    fig.show()


def sid_region(records):
    conn = sqlite3.connect(INSTANCES_DB)
    c = conn.cursor()
    count = 0
    exceptions = []
    for key, val in records.items():
        router = val['sid_router']
        server = val['sid_server']
        c.execute("select region from instances where primaryIpv4Pub = '{}'".format(server))
        server_region = c.fetchone()[0]
        c.execute("select region from instances where secondaryIpv4Pub = '{}'".format(router))
        router_region = c.fetchone()[0]
        if router_region != server_region:
            exceptions.append(key)
            count += 1
            print('{} -> {}'.format(REGIONS[router_region], REGIONS[server_region]))
            print(val['ping'])
    print("region change: {}/{}".format(count, len(records.keys())))
    print("exceptions = " + str(exceptions))


latency_map = parse_local_dns_latency()


def main():
    records = parse()
    print(json.dumps(records))
    invalid_hosts = [key for key, val in records.items() if all(x == 0 for x in val['sid_data'])]
    print('Invalid data: {}/{}'.format(len(invalid_hosts), len(records.keys())))
    for host in invalid_hosts:
        records.pop(host)
    exceptions = ['stella.planetlab.ntua.gr', 'vicky.planetlab.ntua.gr', 'planetlab1.dtc.umn.edu',
                  'planetlab-5.eecs.cwru.edu', 'plink.cs.uwaterloo.ca', 'planetlabone.ccs.neu.edu',
                  'planetlab2.dtc.umn.edu', 'node1.planetlab.mathcs.emory.edu', 'node2.planetlab.mathcs.emory.edu',
                  'pl1.rcc.uottawa.ca', 'planetlab5.eecs.umich.edu', 'planetlab3.rutgers.edu',
                  'planetlab-js1.cert.org.cn', 'planetlab2.utdallas.edu', 'planetlab3.eecs.umich.edu',
                  'planetlab1.utdallas.edu']
    exceptions = exceptions + ['planetlab2.cs.purdue.edu', 'planetlab1.cs.purdue.edu', 'planetlab-n1.wand.net.nz']
    compare({key: val for key, val in records.items() if key not in exceptions})
    # compare(records)
    # sid_region(records)


if __name__ == '__main__':
    main()
