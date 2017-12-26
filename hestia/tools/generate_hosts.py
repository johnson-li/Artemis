#!/usr/bin/env python

import sqlite3
import os

from hestia import RESOURCE_PATH, ANSIBLE_PATH
from hestia.aws.regions import REGIONS

DB_PATH = RESOURCE_PATH + '/db'
DB_FILE = DB_PATH + '/instances.db'
HOSTS_FILE = ANSIBLE_PATH + '/inventory/hosts.yml'


def main():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    open(HOSTS_FILE, 'w').close()
    f = open(HOSTS_FILE, 'a')
    f.write('[server]\n')
    c.execute("SELECT * FROM instances WHERE name = 'server'")
    for record in c.fetchall():
        record = dict(zip([d[0] for d in c.description], record))
        line = '{}-{} ansible_port=22 ansible_user=ubuntu ansible_host={} ansible_private_key_file=~/keys/{}.pem' \
            .format(REGIONS[record['region']].lower(), record['name'], record['primaryIpv4Pub'],
                    REGIONS[record['region']].lower())
        f.write(line + '\n')
    f.write('\n[router]\n')
    c.execute("SELECT * FROM instances WHERE name = 'router'")
    for record in c.fetchall():
        record = dict(zip([d[0] for d in c.description], record))
        line = '{}-{} ansible_port=22 ansible_user=ubuntu ansible_host={} ansible_private_key_file=~/keys/{}.pem' \
            .format(REGIONS[record['region']].lower(), record['name'], record['primaryIpv4Pub'],
                    REGIONS[record['region']].lower())
        f.write(line + '\n')
    f.close()


if __name__ == '__main__':
    main()
