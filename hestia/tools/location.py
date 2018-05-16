import json


def get_location(ip):
    f = open('/Users/johnson/huawei-data/exp7/location/' + ip, encoding='utf-8')
    j = json.load(f)
    return j


def main():
    print(get_location('108.162.227.238'))


if __name__ == '__main__':
    main()
