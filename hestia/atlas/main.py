import json
from urllib import request
from urllib.parse import urlencode

from hestia import OUTPUT_PATH
from hestia.atlas.secret import SECRET

MEASUREMENT_PATH = OUTPUT_PATH + '/measurement.data'


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


def main():
    # data = get_measurements()
    data = get_results(12035884)
    with open(MEASUREMENT_PATH, 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    main()
