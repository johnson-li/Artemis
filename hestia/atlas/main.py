import concurrent.futures
import functools
import json
import re
import sqlite3
from math import radians, sin, cos, acos
from urllib import request
from urllib.parse import urlencode

import numpy

from hestia import OUTPUT_PATH, RESOURCE_PATH
from hestia.atlas.secret import SECRET
from hestia.aws.regions import LOCATION, REVERSE_REGIONS

MEASUREMENT_PATH = OUTPUT_PATH + '/measurement.data'
REGION_PATH = OUTPUT_PATH + '/region.data'
REGION_ASN_PATH = OUTPUT_PATH + '/region-asn.data'
PING_MESH_PATH = OUTPUT_PATH + '/ping-mesh.log'
ASN_INFO_PATH = OUTPUT_PATH + '/asn-info.data'
MEASUREMENT_ASN_PATH = OUTPUT_PATH + '/measurement-asn.data'
NEAREST_PATH = OUTPUT_PATH + '/measurement-nearest.data'
INSTANCES_DB = RESOURCE_PATH + '/db/instances.db'

executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)


def distance(la1, lo1, la2, lo2):
    slat = radians(float(la1))
    slon = radians(float(lo1))
    elat = radians(float(la2))
    elon = radians(float(lo2))
    dist = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
    return dist


@functools.lru_cache(maxsize=8192, typed=False)
def get_asn_info(asn):
    params = urlencode({'resource': asn})
    req = request.Request('https://stat.ripe.net/data/as-overview/data.json?' + params, method='GET')
    resp = request.urlopen(req).read().decode('utf-8')
    return json.loads(resp)['data']


@functools.lru_cache(maxsize=8192, typed=False)
def get_asn(ip):
    params = urlencode({'resource': ip})
    req = request.Request('https://stat.ripe.net/data/network-info/data.json?' + params, method='GET')
    resp = request.urlopen(req).read().decode('utf-8')
    return json.loads(resp)['data']['asns']


@functools.lru_cache(maxsize=8192, typed=False)
def get_geo(ip):
    params = urlencode({'resource': ip})
    req = request.Request('https://stat.ripe.net/data/geoloc/data.json?' + params, method='GET')
    resp = request.urlopen(req).read().decode('utf-8')
    locations = json.loads(resp).get('data', {}).get('locations', [])
    return locations[0] if locations else None


@functools.lru_cache(maxsize=8192, typed=False)
def get_region(ip):
    conn = sqlite3.connect(INSTANCES_DB)
    c = conn.cursor()
    c.execute("select region from main.instances where primaryIpv4Pub = '%s'" % ip)
    for record in c.fetchall():
        return record[0]


def get_measurements():
    params = urlencode({'key': SECRET})
    req = request.Request('https://atlas.ripe.net/api/v2/measurements/my?' + params, method='GET')
    resp = request.urlopen(req).read().decode('utf-8')
    return json.loads(resp)


def get_measurement(mid):
    req = request.Request('https://atlas.ripe.net/api/v2/measurements/%d/' % mid, method='GET')
    resp = request.urlopen(req).read().decode('utf-8')
    return json.loads(resp)


def get_results(mid):
    measurement = get_measurement(mid)
    result_url = measurement['result']
    req = request.Request(result_url)
    resp = request.urlopen(req).read().decode('utf-8')
    return json.loads(resp)


def find_nearest(la, lo):
    distances = []
    for key, val in LOCATION.items():
        distances.append((key, distance(la, lo, val[0], val[1])))
    distances = sorted(distances, key=lambda x: x[1])
    return [item[0] for item in distances][:3]


def get_nearest_location(data):
    hops = data['hops']
    for hop in reversed(hops):
        if hop['ip'] and hop['asn']:
            ip = hop['ip'][0]
            asn = hop['asn'][0]
            asn_info = get_asn_info(asn)
            holder = asn_info['holder']
            if 'amazon' in holder.lower():
                continue
            print(ip + " " + holder)
            location = get_geo(ip)
            nearest = find_nearest(location['latitude'], location['longitude'])
            return {'probe': data['probe'], "nearest": nearest}
    return {}


def parse_traceroute(traceroute_record):
    traceroute_data = traceroute_record['result']
    traceroute = {'probe': traceroute_record['prb_id'], 'target': get_region(traceroute_record['dst_addr']), 'hops': []}
    for hop_data in traceroute_data:
        hop = {}
        pings = hop_data['result']
        hop['ip'] = list({data['from'] for data in pings if 'rtt' in data})
        if hop['ip']:
            hop['asn'] = []
            for ip in hop['ip']:
                for asn in get_asn(ip):
                    hop['asn'].append(asn)
            hop['rtt'] = numpy.median([float(data['rtt']) for data in pings if 'rtt' in data])
            traceroute['hops'].append(hop)
            traceroute['latency'] = hop['rtt']
    traceroute['ip_trace'] = [hop['ip'] for hop in traceroute['hops'] if hop['ip']]
    traceroute['asn_trace'] = [hop['asn'] for hop in traceroute['hops'] if hop['asn']]
    return traceroute


def parse_record(record):
    record = [item for item in record if 'error' not in item['result'][0]]
    traceroutes = []
    futures = [executor.submit(parse_traceroute, traceroute_record) for traceroute_record in record]
    for future in futures:
        try:
            traceroute = future.result()
            traceroutes.append(traceroute)
            print(traceroute)
        except Exception as e:
            print(e)
    json.dump(traceroutes, open(MEASUREMENT_ASN_PATH, 'w'))


def ping_mesh():
    with open(PING_MESH_PATH) as f:
        data = {}
        for line in f.readlines():
            line = line.strip()
            match = re.match('\[([a-z]+)-router\] out: ([0-9.]+) ([0-9.]+)', line)
            if match:
                lo, ip, ttl = match.groups()
                region_from = REVERSE_REGIONS[lo]
                region_to = get_region(ip)
                data.setdefault(region_from, {})[region_to] = ttl
        return data


def main_measurements():
    """
    Get the measurement data (traceroute from probe to the anycast server)
    """
    data = get_results(12035884)
    with open(MEASUREMENT_PATH, 'w') as f:
        json.dump(data, f, indent=2)


def main_asn():
    """
    Assign the IP to the ASN
    """
    data = json.load(open(MEASUREMENT_PATH))
    parse_record(data)


def main_nearest():
    """
    Find the nearest region that the client request heads to
    """
    data = json.load(open(MEASUREMENT_ASN_PATH))
    futures = [executor.submit(get_nearest_location, record) for record in data]
    nearest_data = []
    for future in futures:
        try:
            nearest = future.result()
            nearest_data.append(nearest)
        except Exception as e:
            print(e)
    json.dump(nearest_data, open(NEAREST_PATH, 'w'))


def main_experiment_probe():
    """
    Generate Atlas data for further experiment
    1. Each client will traceroute to the nearest 3 regions
    2. Each client will ping all of the regions
    """
    data = json.load(open(NEAREST_PATH))
    result = {region: [] for region in LOCATION.keys()}
    for item in data:
        if item:
            for region in item['nearest']:
                result[region].append(item['probe'])
    for key, val in result.items():
        print('%s %d' % (key, len(val)))
    print(data[0])
    print([item['probe'] for item in data if item])


def probe_dump_data():
    ids = [12043444, 12043459, 12043461, 12043462, 12043463, 12043464, 12043466, 12043467, 12043468,
           12043469, 12043470, 12043471, 12043473, 12043475, 12043476]
    measurements = {mid: get_results(mid) for mid in ids}
    json.dump(measurements, open(REGION_PATH, 'w'))


def probe_add_asn():
    measurements = json.load(open(REGION_PATH))
    data = {}
    futures = []
    for mid, measurement in measurements.items():
        for record in measurement:
            futures.append(executor.submit(parse_traceroute, record))
    for future in futures:
        traceroute = future.result()
        data.setdefault(traceroute['probe'], []).append(traceroute)
        print('%s %s' % (traceroute['probe'], traceroute['target']))
    json.dump(data, open(REGION_ASN_PATH, 'w'))


def match_any(set1, set2):
    if not set1:
        return False
    for item in set1:
        if item in set2:
            return True
    return False


def compare_traceroute(asn_trace1, asn_trace2):
    """
    Compare two traceroutes and determine if they follow the same route
    """
    # print('%s\n--%s' % (asn_trace1['ip_trace'], asn_trace2['ip_trace']))
    trace1 = []
    trace2 = []
    pre = None
    if not asn_trace1['hops'] or not asn_trace2['hops']:
        return False
    for asn in asn_trace1['asn_trace'][0]:
        if not match_any(pre, asn):
            pre = asn
            trace1.append(asn)
    pre = None
    for asn in asn_trace2['asn_trace'][0]:
        if not match_any(pre, asn):
            pre = asn
            trace2.append(asn)
    if len(trace1) != len(trace2):
        return False
    for i in range(len(trace1)):
        if not match_any(trace1[i], trace2[i]):
            return False
    return True


def probe_analyse_traceroute():
    region_data = json.load(open(REGION_ASN_PATH))
    region_data = {int(key): val for key, val in region_data.items()}
    anycast_data = json.load(open(MEASUREMENT_ASN_PATH))
    anycast_data = {item['probe']: item for item in anycast_data}
    for probe, regions in region_data.items():
        anycast = anycast_data[probe]
        matched_regions = [anycast]
        for region in regions:
            if compare_traceroute(region, anycast):
                matched_regions.append(region)
        print('matched num: %s, %d' % (probe, len(matched_regions)))


def asn_info():
    result = {}
    region_data = json.load(open(REGION_ASN_PATH))
    anycast_data = json.load(open(MEASUREMENT_ASN_PATH))
    futures = []
    for probe, regions in region_data.items():
        for region in regions:
            for asn in region['asn_trace']:
                for num in asn:
                    if num not in result:
                        futures.append(executor.submit(get_asn_info, num))
    for data in anycast_data:
        for asn in data['asn_trace']:
            for num in asn:
                if num not in result:
                    futures.append(executor.submit(get_asn_info, num))
    for future in futures:
        asn_data = future.result()
        if asn_data['resource'] not in result:
            result[asn_data['resource']] = asn_data
    json.dump(result, open(ASN_INFO_PATH, 'w'))


def main_probe():
    """
    Analysis data of tracerouting probe to EC2 zones
    """
    # probe_dump_data()
    # probe_add_asn()
    # asn_info()
    probe_analyse_traceroute()


def main_latency():
    region_data = json.load(open(REGION_PATH))
    anycast_data = json.load(open(MEASUREMENT_PATH))
    latencies = {}
    for _, regions in region_data.items():
        for region in regions:
            probe = region['prb_id']
            last = region['result'][-1]
            rtts = [item['rtt'] for item in last['result'] if 'rtt' in item]
            if not rtts:
                continue
            med = numpy.median(rtts)
            latency = latencies.setdefault(probe, {}).setdefault('latency', {}).get('unicast', 10000)
            if med < latency:
                latency = med
                # region_name = region['']
                latencies[probe]['latency']['unicast'] = latency
    for region in anycast_data:
        probe = region['prb_id']
        last = region['result'][-1]
        if 'error' in last:
            continue
        rtts = [item['rtt'] for item in last['result'] if 'rtt' in item]
        if not rtts:
            continue
        med = numpy.median(rtts)
        latency = latencies.setdefault(probe, {}).setdefault('latency', {}).get('anycast', 10000)
        if med < latency:
            latency = med
            # region_name = region['']
            latencies[probe]['latency']['anycast'] = latency
    print(json.dumps(latencies))
    # unicast_values = [val['latency']['unicast'] for val in latencies.values() if
    #                   'unicast' in val['latency'] and 'anycast' in val['latency']]
    # anycast_values = [val['latency']['anycast'] for val in latencies.values() if
    #                   'unicast' in val['latency'] and 'anycast' in val['latency']]
    # print('unicast = %s;' % unicast_values)
    # print('anycast = %s;' % anycast_values)


def main_last_ip():
    anycast_data = json.load(open(MEASUREMENT_ASN_PATH))
    ips = set()
    for data in anycast_data:
        ip = (data['ip_trace'][-2] if len(data['ip_trace']) > 1 else [])
        if ip:
            ips.add(ip[0])
    ips = sorted(list(ips))
    print(ips)


def main():
    # main_measurements()
    # main_asn()
    # main_nearest()
    # main_experiment_probe()
    # main_probe()
    # main_latency()
    main_last_ip()


if __name__ == '__main__':
    main()
