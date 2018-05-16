import os
from multiprocessing import Pool


def mtr(host):
    print(host)
    os.system('sudo mtr -nj -i 0.2 -c 5 %s > /Users/johnson/huawei-data/exp7/traceroute/%s' % (host, host))


def main():
    f = open('/Users/johnson/huawei-data/exp7/traceroute/hosts')
    hosts = set()
    for line in f.readlines():
        line = line.rstrip()
        hosts.add(line)
    hosts = list(hosts)
    with Pool(8) as pool:
        pool.map(mtr, hosts)


if __name__ == '__main__':
    main()
