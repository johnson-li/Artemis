#!/usr/bin/env python

import argparse
import os
import sqlite3

from hestia import RESOURCE_PATH, ANSIBLE_PATH
from hestia.aws.regions import REGIONS

DB_PATH = RESOURCE_PATH + '/db'
DB_FILE = DB_PATH + '/instances.db'
HOSTS_FILE = ANSIBLE_PATH + '/inventory/hosts.yml'
CONFIG_FILE = RESOURCE_PATH + '/ssh/config'
CONFIG_FILE_6 = RESOURCE_PATH + '/ssh/config6'
PLATFORM = 'AWS'


def generate_ansible_hosts():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    open(HOSTS_FILE, 'w').close()
    f = open(HOSTS_FILE, 'a')
    f.write('[server]\n')
    c.execute("SELECT * FROM instances WHERE name = 'server'")
    for record in c.fetchall():
        record = dict(zip([d[0] for d in c.description], record))
        line = '{}-{} ansible_port=22 ansible_user={} ansible_host={} ansible_private_key_file={}' \
            .format(REGIONS[record['region']].lower() if PLATFORM == 'AWS' else record['region'], record['name'],
                    'ubuntu' if PLATFORM == 'AWS' else 'johnsonli1993', record['primaryIpv4Pub'],
                    '~/keys/%s.pem' % REGIONS[record['region']].lower() if PLATFORM == 'AWS' else '~/.ssh/id_rsa')
        f.write(line + '\n')
    f.write('\n[router]\n')
    c.execute("SELECT * FROM instances WHERE name = 'router'")
    for record in c.fetchall():
        record = dict(zip([d[0] for d in c.description], record))
        line = '{}-{} ansible_port=22 ansible_user={} ansible_host={} ansible_private_key_file={}' \
            .format(REGIONS[record['region']].lower() if PLATFORM == 'AWS' else record['region'], record['name'],
                    'ubuntu' if PLATFORM == 'AWS' else 'johnsonli1993', record['primaryIpv4Pub'],
                    '~/keys/%s.pem' % REGIONS[record['region']].lower() if PLATFORM == 'AWS' else '~/.ssh/id_rsa')
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
        f.write('Host {}-{}\n'.format(REGIONS[record['region']].lower() if PLATFORM == 'AWS' else
                                      record['region'], record['name']))
        f.write('  HostName {}\n'.format(record['primaryIpv4Pub']))
        f.write('  User {}\n'.format('ubuntu' if PLATFORM == 'AWS' else 'johnsonli1993'))
        f.write('  IdentityFile {}\n'.format(
            '~/keys/%s.pem' % (REGIONS[record['region']].lower()) if PLATFORM == 'AWS' else '~/.ssh/id_rsa'))
        f.write('\n')
    if os.path.exists(CONFIG_FILE_6):
        open(CONFIG_FILE_6, 'w').close()
    f = open(CONFIG_FILE_6, 'a')
    c.execute("SELECT * FROM instances")
    for record in c.fetchall():
        record = dict(zip([d[0] for d in c.description], record))
        f.write('Host {}-{}\n'.format(REGIONS[record['region']].lower() if PLATFORM == 'AWS' else
                                      record['region'], record['name']))
        f.write('  HostName {}\n'.format(record['primaryIpv6']))
        f.write('  User ubuntu\n')
        f.write('  IdentityFile {}\n'.format(
            '~/keys/%s.pem' % (REGIONS[record['region']].lower()) if PLATFORM == 'AWS' else '~/.ssh/id_rsa'))
        f.write('\n')


def main():
    global PLATFORM
    global DB_FILE
    parser = argparse.ArgumentParser(description='Generate the host file.')
    parser.add_argument('--platform', dest='platform', type=str, default='AWS', choices=['AWS', 'GCP'],
                        help='the cloud platform, GCP or AWS')
    args = parser.parse_args()
    PLATFORM = args.platform
    if PLATFORM == 'GCP':
        DB_FILE = DB_PATH + '/gcp_instances.db'
    generate_ansible_hosts()
    generate_ssh_hosts()


if __name__ == '__main__':
    main()
