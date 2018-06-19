import json
import random

import grequests

from hestia import OUTPUT_PATH

PROBES_PATH = OUTPUT_PATH + "/probes.data"


def download_probes():
    requests = []
    for index in range(1, 256):
        url = "https://atlas.ripe.net/api/v2/probes/?page=" + str(index)
        requests.append(grequests.get(url, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}))
    responses = grequests.map(requests)
    results = []
    for response in responses:
        j = json.loads(response.text)
        results += j['results']
    json.dump(results, open(PROBES_PATH, 'w'))


def get_probes():
    return json.load(open(PROBES_PATH))


def sample(results):
    asn_map = {}
    for result in results:
        asn = result['asn_v4']
        if asn:
            asn_map.setdefault(asn, []).append(result['id'])
    result = {key: random.choice(val) for key, val in asn_map.items()}
    data = set()
    while len(data) < 1000:
        data.add(random.choice(list(result.values())))
    return data


def main():
    results = get_probes()
    results = list(filter(lambda x: x.get('status', {}).get('name', '') == 'Connected', results))
    print(len(results))
    print(results[0])
    probes = sample(results)
    print(probes)


if __name__ == '__main__':
    main()
