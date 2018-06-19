import functools
import json
import random
import re
import statistics
from urllib import request
from urllib.parse import urlencode

import geopy.distance
import grequests

import hestia.tools.location
from hestia.atlas.secret import SECRET

unicast_mesh = {}
anycast_mesh = {}  # 1.1.1.1
anycast_match = {}
optimal_match = {}
anycast_hops = {}
unicast_hops = {}
routers = {}
routers_reverse = {}


def get_city(ip):
    j = json.load(open('/Users/johnson/huawei-data/exp7/location/' + ip, encoding='utf-8'))
    city = j.get('city', {})
    name = city.get('names', {}).get('en', '')
    if not name:
        print('invalid location data: ' + ip)
    return name


def get_distance(ip1, ip2):
    j1 = json.load(open('/Users/johnson/huawei-data/exp7/location/' + ip1, encoding='utf-8'))
    j2 = json.load(open('/Users/johnson/huawei-data/exp7/location/' + ip2, encoding='utf-8'))
    coords1 = (j1['location']['latitude'], j1['location']['longitude'])
    coords2 = (j2['location']['latitude'], j2['location']['longitude'])
    # print('%s %s %s %s' % (ip1, ip2, j1['city']['names']['en'], j2['city']['names']['en']))
    return geopy.distance.vincenty(coords1, coords2).m


def get_latency(ip1, ip2):
    """
    :return: minimal latency between ip1 and ip2, limited by the speed of light
    """
    return get_distance(ip1, ip2) * 1000 / 299792458


@functools.lru_cache()
def get_measurements(url=None):
    result = []
    if not url:
        params = urlencode({'key': SECRET})
        url = 'https://atlas.ripe.net/api/v2/measurements/my?' + params
    req = request.Request(url, method='GET')
    resp = request.urlopen(req).read().decode('utf-8')
    j = json.loads(resp)
    result += j['results']
    if j['next']:
        result += get_measurements(j['next'])
    return result


def ping(target):
    ids = get_probes()
    return grequests.post('https://atlas.ripe.net/api/v2/measurements//?key=' + SECRET, json={
        "definitions": [
            {
                "target": target,
                "af": 4,
                "packets": 1,
                "size": 48,
                "description": "Ping measurement to %s" % target,
                "tags": ["ping-unicast-7"],
                "resolve_on_probe": False,
                "skip_dns_check": False,
                "include_probe_id": False,
                "type": "ping"
            }
        ],
        "probes": [
            {
                "type": "probes",
                "value": ','.join([str(i) for i in ids]),
                "requested": len(ids)
            }
        ],
        "is_oneoff": True,
        "bill_to": "johnsonli1993@gmail.com"
    }, headers={'Content-Type': 'application/json', 'Accept': 'application/json'})


def traceroute(prbs, target):
    return grequests.post('https://atlas.ripe.net/api/v2/measurements//?key=' + SECRET, json={
        "definitions": [
            {
                "target": target,
                "af": 4,
                "timeout": 4000,
                "description": "Traceroute measurement to " + target,
                "protocol": "ICMP",
                "tags": ['traceroute-5'],
                "resolve_on_probe": False,
                "packets": 1,
                "size": 48,
                "first_hop": 1,
                "max_hops": 32,
                "paris": 16,
                "destination_option_size": 0,
                "hop_by_hop_option_size": 0,
                "dont_fragment": False,
                "skip_dns_check": False,
                "type": "traceroute"
            }
        ],
        "probes": [
            {
                "value": str(','.join([str(i) for i in prbs])),
                "type": "probes",
                "requested": len(prbs)
            }
        ],
        "is_oneoff": True,
        "bill_to": "johnsonli1993@gmail.com"
    })


def create_measurement_request(probe):
    return grequests.post('https://atlas.ripe.net/api/v2/measurements/?key=' + SECRET, json={
        "definitions": [
            {
                "target": "1.1.1.1",
                "af": 4,
                "query_class": "IN",
                "query_type": "A",
                "query_argument": ("%d.sec.xuebing.name" % probe),
                "use_macros": True,
                "description": "DNS measurement to 1.1.1.1, by %d" % probe,
                "tags": ["cf-dns-demo"],
                "use_probe_resolver": False,
                "resolve_on_probe": False,
                "set_nsid_bit": True,
                "protocol": "UDP",
                "udp_payload_size": 512,
                "retry": 0,
                "skip_dns_check": False,
                "include_qbuf": True,
                "include_abuf": True,
                "prepend_probe_id": True,
                "set_rd_bit": True,
                "set_do_bit": True,
                "set_cd_bit": True,
                "timeout": 5000,
                "type": "dns"
            }
        ],
        "probes": [
            {
                "value": str(probe),
                "type": "probes",
                "requested": 1
            }
        ],
        "is_oneoff": True,
        "bill_to": "johnsonli1993@gmail.com"
    }, headers={'Content-Type': 'application/json', 'Accept': 'application/json'})


def get_probes():
    f = open('/Users/johnson/huawei-data/exp7/anycast.json')
    j = json.load(f)
    ids = []
    for item in j:
        ids.append(item['prb_id'])
    return ids


def conduct_experiment():
    ids = get_probes()
    requests = [create_measurement_request(probe) for probe in ids[10:11]]
    for request in requests:
        print(request)
    responses = grequests.map(requests)
    for response in responses:
        print(response.text)


def parse_tcpdump():
    f = open('/Users/johnson/huawei-data/exp7/cloudflare.records')
    ips = set()
    for line in f.readlines():
        match = re.match('.*IP ([0-9.]+)', line)
        if match:
            ip = re.match('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', match.groups()[0]).group(0)
            probe = re.search('(\d+)\.\d+\.aa\.sec\.xuebing\.name', line).group(1)
            ips.add(ip)
            anycast_match[int(probe)] = ip
    return list(ips)


def get_targets():
    hosts = parse_tcpdump()
    targets = {}
    for host in hosts:
        last = host
        prefix = last[:last.rfind('.')]
        if prefix not in targets:
            targets[prefix] = last
    return targets.values()


def ping_unicast():
    targets = get_targets()
    requests = [ping(target) for target in targets]
    responses = grequests.map(requests)
    for response in responses:
        print(response.text)


def minimal_rtt(record):
    rtts = record['result']
    rtts = [r['rtt'] for r in rtts if 'rtt' in r.keys()]
    return minimal(rtts)


def parse_unicast_result(result):
    for record in result:
        prb = record['prb_id']
        dst = record['dst_addr']
        unicast_mesh.setdefault(prb, {})
        if dst not in unicast_mesh[prb]:
            unicast_mesh[prb][dst] = minimal_rtt(record)
        else:
            unicast_mesh[prb][dst] = min(minimal_rtt(record), unicast_mesh[prb][dst])


def parse_unicast_results():
    with open('/Users/johnson/huawei-data/exp7/unicast2/measurements') as ff:
        for line in ff.readlines():
            mid = line.strip()
            parse_unicast_result(json.load(open("/Users/johnson/huawei-data/exp7/unicast2/" + mid)))
    with open('/Users/johnson/huawei-data/exp7/unicast/measurements') as ff:
        for line in ff.readlines():
            mid = line.strip()
            parse_unicast_result(json.load(open("/Users/johnson/huawei-data/exp7/unicast/" + mid)))


def parse_anicast_results():
    global anycast_mesh
    result = json.load(open('/Users/johnson/huawei-data/exp7/anycast.json'))
    anycast_mesh = {i['prb_id']: minimal_rtt(i) for i in result}


def minimal(items):
    if items:
        return min(items)
    return -3


def traceroute_all():
    requests = []
    pairs = {}
    for prb, dst in anycast_match.items():
        pairs.setdefault(dst, []).append(prb)
    for dst, prbs in pairs.items():
        requests.append(traceroute(prbs, dst))
    responses = grequests.map(requests)
    for response in responses:
        print(response.text)


def parse_hops():
    j = json.load(open('/Users/johnson/huawei-data/exp7/traceroute/anycast.json'))
    for record in j:
        hops = record['result']
        hops = [hop['result'][0]['from'] for hop in hops if 'from' in hop['result'][0]]
        prb = int(record['prb_id'])
        anycast_hops[prb] = hops
    for mid in open('/Users/johnson/huawei-data/exp7/traceroute/measurements').readlines():
        mid = int(mid)
        j = json.load(open('/Users/johnson/huawei-data/exp7/traceroute/' + str(mid)))
        for record in j:
            hops = record['result']
            hops = [hop['result'][0]['from'] for hop in hops if 'from' in hop['result'][0]]
            prb = int(record['prb_id'])
            unicast_hops[prb] = hops


def hops_match(hops1, hops2):
    if len(hops1) == len(hops2) == 1:
        return True
    if len(hops1) == 1 or len(hops2) == 1:
        return False
    if hops1[-2] == hops2[-2]:
        return True
    if hops1[-2] == hops2[-1]:
        return True
    if hops1[-1] == hops2[-2]:
        return True


def matched_probes():
    result = []
    for key in anycast_hops:
        if key in unicast_hops:
            if hops_match(anycast_hops[key], unicast_hops[key]):
                result.append(key)
    # result.remove(27636)
    return result


def get_by_subnet(mesh, target):
    value = 10000
    for key in mesh:
        # if key == target:
        if key[:key.rfind('.')] == target[:target.rfind('.')]:
            if mesh[key] < value:
                value = mesh[key]
    return value


def parse_traceroute_local(ids):
    hosts = []
    for line in open('/Users/johnson/huawei-data/exp7/traceroute-local/hosts').readlines():
        hosts.append(line.strip())
    for host in hosts:
        j = json.load(open('/Users/johnson/huawei-data/exp7/traceroute-local/' + host))
        router = j['report']['hubs'][-2]['host']
        routers.setdefault(router, []).append(host)
        routers_reverse[host] = router
    print('routers: ' + str(len(routers)))
    print(routers)
    print({key: set([hestia.tools.location.get_location(v).get('city', {}).get('names', {}).get('en', '') for v in val])
           for key, val in routers.items()})
    print(sorted(routers.keys()))


def get_solutions(n, limit):
    if n == 1:
        return [[l] for l in list(range(limit))]
    pre = get_solutions(n - 1, limit)
    solutions = []
    for i in range(limit):
        for pp in pre:
            if i not in pp:
                solutions.append([i] + pp)
    return solutions


def best_deployment(keys):
    candidates = [r[0] for r in routers.values()]

    mean = {}
    median = {}
    for i in range(1, 26):
        mean[i] = 500
        median[i] = 500
    for i in range(100):
        print('iter: %d' % i)
        for number in range(1, 26):
            solutions = set()
            count = 0
            while count < number:
                index = random.randint(1, len(candidates) - 1)
                if index not in solutions:
                    solutions.add(index)
                    count += 1
            data = []
            for key in keys:
                minimal_latency = 1000
                for index in solutions:
                    latency = get_by_subnet(unicast_mesh[key], candidates[index])
                    if 0 < latency < minimal_latency:
                        minimal_latency = latency
                if minimal_latency != 1000:
                    data.append(minimal_latency)
            if len(data) > 10:
                mea = statistics.mean(data)
                med = statistics.median(data)
                if mea < mean[number]:
                    mean[number] = mea
                if med < median[number]:
                    median[number] = med
        print('avg: %s, med: %s' % (str(mean), str(median)))


def main():
    # print(get_latency('162.158.104.70', '172.68.12.187'))
    # ping_unicast()
    # return
    parse_tcpdump()
    parse_unicast_results()
    parse_anicast_results()
    parse_hops()
    # print(unicast_hops[25209])
    # print(anycast_hops[25209])
    valid = matched_probes()
    parse_traceroute_local(valid)
    # print('unicast mesh: ' + str(unicast_mesh[13499]))
    # print('anycast mesh: ' + str(anycast_mesh))
    optimal = {key: minimal([i for i in val.values() if i > 0]) for key, val in unicast_mesh.items()}
    print('optimal: ' + str(optimal))
    optimal_match = {key: list(val.keys())[list(val.values()).index(optimal[key])] for key, val in unicast_mesh.items()}
    # print('optimal match: ' + str(optimal_match))
    # print('anycast match: ' + str(anycast_match))
    diff = {}
    for key in valid:
        if key in anycast_match and key in optimal_match and key in anycast_mesh \
                and anycast_mesh[key] > 0 and key in optimal and optimal[key] > 0 \
                and get_by_subnet(unicast_mesh[key], anycast_match[key]) > 0:
            diff[key] = anycast_mesh[key] - optimal[key]
    print('diff: ' + str(diff))
    print('diff values: ' + str(sorted(diff.values())))
    print("valid: " + str(len(diff)))
    best_deployment(diff.keys())
    return
    anycast = {key: get_by_subnet(unicast_mesh[key], anycast_match[key]) for key in diff}
    optimal = {key: val for key, val in optimal.items() if key in anycast}
    diff_fixed = {key: anycast[key] - optimal[key] for key in anycast}
    nonmatched = {}
    for key in diff:
        anycast_target = anycast_match[key]
        optimal_target = optimal_match[key]
        # if anycast[key] > optimal[key]:
        if routers_reverse[anycast_target] != routers_reverse[optimal_target]:
            print('%s vs %s' % (anycast_target, optimal_target))
            print('%s vs %s,\t%s vs %s' % (
                routers_reverse[anycast_target], routers_reverse[optimal_target], get_city(anycast_target),
                get_city(optimal_target)))
            nonmatched[key] = (anycast[key], optimal[key])
    print("non optimal len: " + str(len(list(filter(lambda x: x > 0, diff_fixed.values())))))
    print('anycast: ' + str(statistics.mean(sorted(anycast.values()))))
    print('optimal: ' + str(statistics.mean(sorted(optimal.values()))))
    print('diff_fixed: ' + str(statistics.mean(sorted(diff_fixed.values()))))
    print(len(anycast))
    distances = {key: get_distance(anycast_match[key], optimal_match[key]) for key in nonmatched}
    print("distances: " + str(sorted(distances.values())))
    # print('non optimal: ' + str(len(diff_match)))
    # print('non optimal: ' + str(diff_match))
    # diff_nonmatched = {
    #     key: (
    #         get_by_subnet(unicast_mesh[key], anycast_match[key]), get_by_subnet(unicast_mesh[key], optimal_match[key]))
    #     for key in diff_match}
    print('nonmatched num: ' + str(len(nonmatched)))
    print('nonmatched anycast: ' + str(sorted([p[0] for p in nonmatched.values()])))
    print('nonmatched optimal: ' + str(sorted([p[1] for p in nonmatched.values()])))
    print('nonmatched diff: ' + str(statistics.mean(sorted([p[0] - p[1] for p in nonmatched.values()]))))
    print('nonmatched saved: ' + str(statistics.mean(sorted([(p[0] - p[1]) / p[0] for p in nonmatched.values()]))))
    print('nonmatched saved: ' + str(sorted([(p[0] - p[1]) / p[0] for p in nonmatched.values()])))
    print('nonmatched diff: ' + str(len([p[0] - p[1] for p in nonmatched.values() if p[0] - p[1] > 20])))

    ds = []
    saved = []
    wasted = []
    for key in distances:
        ds.append(distances[key])
        saved.append(diff_fixed[key])
        wasted.append(diff_fixed[key] / 2 - get_latency(anycast_match[key], optimal_match[key]) / 2)
    print('ds: ' + str(ds))
    print('saved: ' + str(saved))
    print('wasted: ' + str(wasted))


if __name__ == '__main__':
    main()
