#!/usr/bin/env python

import os
import sqlite3

from hestia import RESOURCE_PATH, ANSIBLE_PATH
from hestia.aws.regions import REGIONS

DB_PATH = RESOURCE_PATH + '/db'
DB_FILE = DB_PATH + '/instances.db'
HOSTS_FILE = ANSIBLE_PATH + '/inventory/hosts.yml'
CONFIG_FILE = RESOURCE_PATH + '/ssh/config'
CONFIG_FILE_6 = RESOURCE_PATH + '/ssh/config6'


def generate_ansible_hosts():
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


def generate_ssh_hosts():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    if os.path.exists(CONFIG_FILE):
        open(CONFIG_FILE, 'w').close()
    f = open(CONFIG_FILE, 'a')
    c.execute("SELECT * FROM instances")
    for record in c.fetchall():
        record = dict(zip([d[0] for d in c.description], record))
        f.write('Host {}-{}\n'.format(REGIONS[record['region']].lower(), record['name']))
        f.write('  HostName {}\n'.format(record['primaryIpv4Pub']))
        f.write('  User ubuntu\n')
        f.write('  IdentityFile ~/keys/{}.pem\n'.format(REGIONS[record['region']].lower()))
        f.write('\n')
    if os.path.exists(CONFIG_FILE_6):
        open(CONFIG_FILE_6, 'w').close()
    f = open(CONFIG_FILE_6, 'a')
    c.execute("SELECT * FROM instances")
    for record in c.fetchall():
        record = dict(zip([d[0] for d in c.description], record))
        f.write('Host {}-{}\n'.format(REGIONS[record['region']].lower(), record['name']))
        f.write('  HostName {}\n'.format(record['primaryIpv6']))
        f.write('  User ubuntu\n')
        f.write('  IdentityFile ~/keys/{}.pem\n'.format(REGIONS[record['region']].lower()))
        f.write('\n')


def main():
    generate_ansible_hosts()
    generate_ssh_hosts()


if __name__ == '__main__':
    main()
