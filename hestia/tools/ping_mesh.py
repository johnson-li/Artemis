import re
import sqlite3

from prettytable import PrettyTable

from hestia.aws.regions import REGIONS

DB1 = '../../resources/exp1/instances.db'
DB2 = '../../resources/exp1/instances.db2'
F1 = '../../resources/exp1/ping_mesh'
F2 = '../../resources/exp1/ping_mesh_v6'

REGIONS_REV = {REGIONS[key].lower(): key for key in REGIONS.keys()}
RESULT = [[-1 for i in range(len(REGIONS))] for j in range(len(REGIONS))]
# for i in range(len(REGIONS.keys())):
#     RESULT.append([len(REGIONS.keys())])
NAMES = list(REGIONS.keys())


def ping_mesh():
    table = PrettyTable()
    table.add_column(' ', NAMES)
    conn = sqlite3.connect(DB1)
    c = conn.cursor()
    f1 = open(F1)
    for line in f1.readlines():
        if re.match('\[.*router\] out: \d+', line):
            region = re.search('\[(.*)-router\]', line).group(1)
            region = REGIONS_REV[region]
            target = re.search('(\d+\.\d+\.\d+\.\d+)', line).group()
            c.execute("select region from instances where primaryIpv4Pub = '{}'".format(target))
            target = c.fetchone()[0]
            time = re.search('\d+ (\d+.\d+)', line).group(1)
            RESULT[NAMES.index(region)][NAMES.index(target)] = time
    for i in range(len(NAMES)):
        table.add_column(NAMES[i], RESULT[i])
    print(table)


def ping_mesh_v6():
    table = PrettyTable()
    table.add_column(' ', NAMES)
    conn = sqlite3.connect(DB2)
    c = conn.cursor()
    f1 = open(F2)
    for line in f1.readlines():
        if re.match('\[.*router\] out: \d+', line):
            region = re.search('\[(.*)-router\]', line).group(1)
            region = REGIONS_REV[region]
            target = re.search('out: ([0-9:a-f]+)', line).group(1)
            c.execute("select region from instances where primaryIpv6 = '{}'".format(target))
            target = c.fetchone()[0]
            sear = re.search('(\d+\.\d+)', line)
            time = -1
            if sear:
                time = sear.group()
            RESULT[NAMES.index(region)][NAMES.index(target)] = time
    for i in range(len(NAMES)):
        table.add_column(NAMES[i], RESULT[i])
    print(table)


def main():
    ping_mesh()
    ping_mesh_v6()


if __name__ == '__main__':
    main()
