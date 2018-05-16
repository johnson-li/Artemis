import sqlite3

import boto3

from hestia import RESOURCE_PATH

DB_PATH = RESOURCE_PATH + '/db'
DB_FILE = DB_PATH + '/instances.db'


def clear_cdn():
    client = boto3.client('route53')
    while True:
        sets = client.list_resource_record_sets(HostedZoneId="ID:Z1698DP7F9XEFJ")['ResourceRecordSets']
        sets = list(filter(lambda a: a['Type'] == 'A' and a['Name'].endswith('.xuebingli.com.'), sets))
        if sets:
            client.change_resource_record_sets(HostedZoneId="ID:Z1698DP7F9XEFJ", ChangeBatch={
                'Changes': [{'Action': 'DELETE', "ResourceRecordSet": se} for se in sets]})
        else:
            break


def add_cdn():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    sets = []
    c.execute("SELECT * FROM instances")
    for host in c.fetchall():
        host = dict(zip([d[0] for d in c.description], host))
        if host['name'] == 'router':
            record = {'Name': 'cdn%s.xuebingli.com.' % host['region'].replace('-', ''), 'Type': 'A',
                      'TTL': 60, 'ResourceRecords': [{'Value': host['secondaryIpv4Pub']}]}
            sets.append(record)
            for i in range(21):
                record = {'Name': 'cdn%s%d.xuebingli.com.' % (host['region'].replace('-', ''), i), 'Type': 'A',
                          'TTL': 60, 'ResourceRecords': [{'Value': host['secondaryIpv4Pub']}]}
                sets.append(record)
    client = boto3.client('route53')
    client.change_resource_record_sets(HostedZoneId="ID:Z1698DP7F9XEFJ", ChangeBatch={
        'Changes': [{'Action': 'UPSERT', "ResourceRecordSet": se} for se in sets]})


def main():
    clear_cdn()
    add_cdn()


if __name__ == '__main__':
    main()
