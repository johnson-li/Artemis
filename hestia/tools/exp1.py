import json
import re
import sqlite3
import statistics

import matplotlib.pyplot as plt
import numpy

from hestia.aws.regions import REGIONS
from hestia.plt.anycast import ANYCAST_DATA

PATH = '/Users/johnson/huawei-data/exp7'
INSTANCES_DB = PATH + '/instances.db'
REPEAT = 6
PERCENTILE = 90


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
    """
    Parse the experiment log file
    :return:
    """
    records = {}
    for file in ['direct', 'hit', 'miss', 'sid']:
        file = PATH + '/latency/' + file + '.log'
        with open(file) as f:
            for line in f.readlines():
                if line.startswith('Host: '):
                    host = line[6:-1]
                    if host not in records:
                        records[host] = {}
                elif line.startswith('direct_data'):
                    direct_data = line[14:-1]
                    records[host]['direct_data'] = [float(i) for i in direct_data.split(',')]
                elif line.startswith('dns_hit_data'):
                    dns_hit_data = line[15:-1]
                    records[host]['dns_hit_data'] = [float(i) if i else 0 for i in dns_hit_data.split(',')]
                elif line.startswith('dns_hit_delay'):
                    dns_hit_delay = line[16:-1]
                    records[host]['dns_hit_delay'] = [float(i) if i else 0 for i in dns_hit_delay.split(',')]
                elif line.startswith('dns_data'):
                    dns_data = line[11:-1]
                    records[host]['dns_data'] = [float(i) for i in dns_data.split(',')]
                elif line.startswith('dns_delay'):
                    dns_delay = line[12:-1]
                    records[host]['dns_delay'] = [float(i) if i else 0 for i in dns_delay.split(',')]
                elif line.startswith('sid_data'):
                    sid_data = line[11:-1]
                    records[host]['sid_data'] = [float(i) for i in sid_data.split(',')]
                elif line.startswith('direct_server'):
                    records[host]['direct_server'] = line[15:-1]
                elif line.startswith('dns_servers'):
                    dns_servers = line[14:-1]
                    records[host]['dns_servers'] = dns_servers.split(',')
                elif line.startswith('sid_router'):
                    records[host]['sid_router'] = line[12:-1]
                elif line.startswith('sid_server'):
                    records[host]['sid_server'] = line[12:-1]
    return records


def transform(records):
    records = {
        key: [{val_key: val[val_key][i] if isinstance(val.get(val_key, None), list) else val.get(val_key, None) for
               val_key in
               ['direct_data', 'dns_hit_data', 'dns_hit_delay', 'dns_data', 'dns_delay', 'sid_data']} for
              i in range(REPEAT)] for key, val in records.items()}
    for key in records.keys():
        records[key] = list(filter(lambda x: all(i != 0 for i in x.values()), records[key]))
    records = {key: val for key, val in records.items() if val}
    return records


def records_percentile(records, percentile):
    res = {}
    keys = records.keys()
    print(keys)
    for key in keys:
        record = records[key]
        median = {}
        for data_key in record[0].keys():
            if isinstance(record[0][data_key], float):
                data = [record[i][data_key] for i in range(len(record))]
                data = list(filter(lambda x: 0 < x < 4000, data))
                median[data_key] = numpy.percentile(data, percentile)
        median['hit_increment'] = median['dns_hit_data'] - median['direct_data']
        median['sid_increment'] = median['sid_data'] - median['direct_data']
        median['sid_hit_incr'] = median['sid_data'] - median['dns_hit_data']
        res[key] = median
        if median['sid_increment'] < -1 or median['sid_increment'] > 1:
            print('Except: ' + key + " " + str(median['sid_increment']))
    return res


def plot(fig, records, key):
    data = [d[key] for d in records.values()]
    data = sorted(data)
    if key == 'sid_increment':
        print("sid increment mean: " + str(numpy.mean(data)))
    # print({key: {a: b[key] for a, b in records.items()}})
    p = 1. * numpy.arange(len(data)) / (len(data) - 1)
    ax1 = fig.add_subplot(121)
    ax1.plot(data, p, label=key)
    ax1.set_xlabel('Time (ms)')
    ax1.set_ylabel('CDF')
    # ax1.legend(loc="upper left")
    ax1.legend(loc="lower right")


def compare(records):
    records = transform(records)
    print(records)
    records_median = records_percentile(records, PERCENTILE)
    # for key in records_median.values()[0].keys():
    #     print(key + ' = ' + str([v[key] for v in records_median.values()]) + ';')
    # pprint(records_median)
    # print(records_median)
    fig = plt.figure(figsize=(8, 6), dpi=320)
    print(123123)
    print([v['sid_data'] for v in records_median.values()])
    plot(fig, records_median, 'direct_data')
    plot(fig, records_median, 'dns_hit_data')
    plot(fig, records_median, 'dns_data')
    plot(fig, records_median, 'sid_data')
    # plot(fig, records_median, 'dns_delay')
    # plot(fig, latency_map, 'latency')
    # plot(fig, records_median, 'hit_increment')
    # plot(fig, records_median, 'sid_increment')
    # plot(fig, records_median, 'sid_hit_incr')
    # fig.suptitle('Latencies diff (group2-90)')
    plt.savefig('demo.eps', format='eps', dpi=1000, bbox_inches='tight')
    fig.show()
    SID_DATA = 'sid_data'
    print([k for k, v in records_median.items() if v['dns_hit_data'] - v[SID_DATA] < 0])
    print([k for k, v in records_median.items() if v['dns_data'] - v[SID_DATA] < 0])
    hit_incr = [v['dns_hit_data'] - v[SID_DATA] for v in records_median.values()]
    miss_incr = [v['dns_data'] - v[SID_DATA] for v in records_median.values()]
    print('hit_incr = ' + str(statistics.mean([i for i in hit_incr if i > 10])))
    print('miss_incr = ' + str(statistics.mean([i for i in miss_incr if i > 40])))
    print('avg: ' + str(0.835 * statistics.mean([i for i in hit_incr if i > 10]) + 0.165 * statistics.mean(
        [i for i in miss_incr if i > 40])))
    print('sid = ' + str(statistics.mean([v['sid_data'] for v in records_median.values()])))
    print('hit = ' + str(statistics.mean([v['dns_hit_data'] for v in records_median.values()])))
    print('miss = ' + str(statistics.mean([v['dns_data'] for v in records_median.values()])))


def sid_region(records):
    conn = sqlite3.connect(INSTANCES_DB)
    c = conn.cursor()
    count = 0
    exceptions = []
    for key, val in records.items():
        router = val['sid_router']
        # server = val['sid_server']
        # server = router
        # anycast = ANYCAST_DATA.get(key, '')
        # if key not in ANYCAST_DATA:
        #     print('No anycast data: ' + key)
        # c.execute("select region from instances where secondaryIpv4Pub = '{}'".format(server))
        # server_region = c.fetchone()[0]
        # c.execute("select region from instances where secondaryIpv4Pub = '{}'".format(router))
        router_region = c.fetchone()[0]
        if key in ANYCAST_DATA and ANYCAST_DATA[key] != server_region:
            count += 1
            print(key + ': {} -> {}'.format(REGIONS[ANYCAST_DATA[key]], REGIONS[server_region]))
        # if router_region != server_region:
        #     exceptions.append(key)
        #     count += 1
        #     print('{} -> {}'.format(REGIONS[router_region], REGIONS[server_region]))
        # print(val['ping'])
    print("region change: {}/{}".format(count, len(records.keys())))
    print("exceptions = " + str(exceptions))


# latency_map = parse_local_dns_latency()


def main():
    records = parse()
    print(json.dumps(records))
    invalid_hosts = [key for key, val in records.items() if
                     'direct_data' not in val or all(not x or x > 4000 for x in val['direct_data']) or
                     'dns_hit_data' not in val or all(not x or x > 4000 for x in val['dns_hit_data']) or
                     'sid_data' not in val or all(not x or x > 4000 for x in val['sid_data']) or
                     'dns_data' not in val or all(not x or x > 4000 for x in val['dns_data'])
                     ]
    print([records[i] for i in invalid_hosts])
    print('Invalid data: {}/{}'.format(len(invalid_hosts), len(records.keys())))
    for host in invalid_hosts:
        records.pop(host)
    exceptions = ['planetlab02.cs.washington.edu']
    compare({key: val for key, val in records.items() if key not in exceptions})
    # compare({key: val for key, val in records.items() if key in exceptions})
    # print(len(records))
    # sid_region(records)


if __name__ == '__main__':
    main()
