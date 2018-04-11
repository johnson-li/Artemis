from hestia import FABRIC_PATH

ANYCAST_DATA = {}


def parse():
    # f = open(FABRIC_PATH + '/traceroute2.csv', encoding="utf-8")
    f = open(FABRIC_PATH + '/traceroute2.csv')
    for line in f:
        parsed = line.split(',')
        host = parsed[0]
        city = parsed[2]
        if city == 'Ashburn':
            ANYCAST_DATA[host] = 'us-east-1'
        elif city == 'Frankfurt am Main':
            ANYCAST_DATA[host] = 'eu-central-1'
        elif city == 'Tokyo':
            ANYCAST_DATA[host] = 'ap-northeast-1'
        elif city.endswith('o Paulo'):
            ANYCAST_DATA[host] = 'sa-east-1'
        elif city == 'Dublin':
            ANYCAST_DATA[host] = 'eu-west-1'
        elif city == 'Herndon':
            ANYCAST_DATA[host] = 'us-east-1'
        elif city == 'Seattle':  # Not accurate
            ANYCAST_DATA[host] = 'us-west-2'
        elif city == 'San Jose':
            ANYCAST_DATA[host] = 'us-west-1'
        elif city.startswith('Berlin'):
            ANYCAST_DATA[host] = 'eu-central-1'
        elif city == 'Amsterdam':  # Netherlands, but Amazon Data Services Ireland Ltd
            ANYCAST_DATA[host] = 'eu-west-1'
        # For non-aws IPs
        elif city == 'Prague':  # Not accurate
            ANYCAST_DATA[host] = 'eu-central-1'
        elif city.startswith('Ann Arbor'):  # Not accurate
            ANYCAST_DATA[host] = 'us-east-2'
        elif city == 'Saint Neots':
            ANYCAST_DATA[host] = 'eu-west-2'
        elif city == 'London':
            ANYCAST_DATA[host] = 'eu-west-2'
        elif city == 'Southampton':
            ANYCAST_DATA[host] = 'eu-west-2'
        elif city == 'Brooklyn':  # Not accurate
            ANYCAST_DATA[host] = 'us-east-1'
        elif city == 'New York':  # Not accurate
            ANYCAST_DATA[host] = 'us-east-1'
        elif city == 'Princeton':  # Not accurate
            ANYCAST_DATA[host] = 'us-east-1'
        elif city == 'Placerville':
            ANYCAST_DATA[host] = 'us-east-1'
        elif city.startswith('Toronto'):
            ANYCAST_DATA[host] = 'ca-central-1'
        elif city.startswith('Seoul'):
            ANYCAST_DATA[host] = 'ap-northeast-2'
        elif city.startswith('Houston'):  # Not accurate
            ANYCAST_DATA[host] = 'us-west-1'
        elif city.startswith('Fortaleza'):
            ANYCAST_DATA[host] = 'sa-east-1'
        elif city == 'Rockville':  # Not accurate
            ANYCAST_DATA[host] = 'us-east-1'
        elif city == 'San Diego':
            ANYCAST_DATA[host] = 'us-west-1'
        elif city == 'Garland':  # Not accurate
            ANYCAST_DATA[host] = 'us-west-1'
        elif city == 'Athens':  # Not accurate
            ANYCAST_DATA[host] = 'eu-west-1'
        elif city == 'Richmond Hill':
            ANYCAST_DATA[host] = 'ca-central-1'
        elif city == 'Stillwater':
            ANYCAST_DATA[host] = ''
        else:
            print('Unrecognized anycast record: ' + line)
    print('Anycast record: ' + str(ANYCAST_DATA))


parse()
