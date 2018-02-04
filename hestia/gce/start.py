import os
import sqlite3

import googleapiclient.discovery

from hestia import RESOURCE_PATH, SQL_PATH
from hestia.gce.zones import ZONES

PROJECT = 'triton-176509'
SUBNET_TEMPLATE = 'https://www.googleapis.com/compute/beta/projects/%s/regions/%s/subnetworks/default2'
DB_PATH = RESOURCE_PATH + '/db'
DB_FILE = DB_PATH + '/gcp_instances.db'
SQL_FILE = SQL_PATH + '/instances.sql'


def init_db(force=True):
    print('Init DB')
    if not os.path.exists(DB_PATH):
        os.mkdir(DB_PATH)
    if os.path.exists(DB_FILE):
        if not force:
            return
        os.remove(DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    init_sql = ''.join(open(SQL_FILE).readlines())
    c.execute(init_sql)
    c.close()
    conn.close()


def wait_for_operations(compute, project, zone_operations):
    print('Waiting for operation to finish...')
    while len(zone_operations) > 0:
        zone, operation = zone_operations.pop(0)
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation['name']).execute()
        if result['status'] == 'DONE':
            if 'error' in result:
                print(result)
        else:
            zone_operations.append((zone, operation))


def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else []


def stop_instances(compute, project, zones):
    zone_operations = []
    for zone in zones:
        instances = list_instances(compute, project, zone)
        instances = filter(lambda x: x['name'].startswith('exp'), instances)
        for instance in instances:
            if instance['status'] == 'RUNNING':
                print('Stop instance: %s' % instance['name'])
                operation = compute.instances().stop(project=project, zone=zone, instance=instance['name']).execute()
                zone_operations.append((zone, operation))
    wait_for_operations(compute, project, zone_operations)
    print("Instances stopped")


def start_instances(compute, project, zones):
    zone_operations = []
    for zone in zones:
        instances = list_instances(compute, project, zone)
        instances = filter(lambda x: x['name'].startswith('exp'), instances)
        for instance in instances:
            if instance['status'] == 'TERMINATED':
                print('Start instance: %s' % instance['name'])
                operation = compute.instances().start(project=project, zone=zone, instance=instance['name']).execute()
                zone_operations.append((zone, operation))
    wait_for_operations(compute, project, zone_operations)
    print("Instances started")


def delete_instances(compute, project, zone):
    instances = list_instances(compute, project, zone)
    instances = filter(lambda x: x['name'].startswith('exp'), instances)
    for instance in instances:
        # compute.instances().delete(project=project, zone=zone, instance=instance)
        print(instance)


def create_instances(compute, project, zone, num):
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    image_response = compute.images().getFromFamily(project='ubuntu-os-cloud', family='ubuntu-1604-lts').execute()
    source_disk_image = image_response['selfLink']
    config = {
        'name': "exp-%s-%d" % (zone, num),
        'description': '%s_%s' % (zone, 'router' if num == 1 else 'server'),
        'machineType': machine_type,
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }, {
            'network': 'global/networks/custom-network1',
            'subnetwork': SUBNET_TEMPLATE % (project, zone[:-2]),
            # 'accessConfigs': [
            #     {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            # ],
        }],
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],
        'networkTags': ['pass-through', 'pass-through-2']
    }
    operation = compute.instances().insert(project=project, zone=zone, body=config).execute()
    # wait_for_operation(compute, project, zone, operation['name'])


def store_instances(compute, project, zones):
    init_db()
    print('Store instances info')
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    for zone in zones:
        instances = list_instances(compute, project, zone)
        for instance in instances:
            if instance['status'] != 'RUNNING':
                continue
            name = instance['name']
            primary_ipv4 = instance['networkInterfaces'][0]['networkIP']
            primary_ipv4_pub = instance['networkInterfaces'][0]['accessConfigs'][0]['natIP']
            secondary_ipv4 = instance['networkInterfaces'][1]['networkIP']
            secondary_ipv4_pub = instance['networkInterfaces'][1]['accessConfigs'][0]['natIP']
            c.execute("INSERT INTO instances (region, name, instanceId, primaryIpv4, primaryIpv6, primaryIpv4Pub, "
                      "secondaryIpv4, secondaryIpv6, secondaryIpv4Pub) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', "
                      "'{}', '{}', '{}')".format(zone, 'router' if name.endswith('1') else 'server', name, primary_ipv4,
                                                 None, primary_ipv4_pub, secondary_ipv4, None, secondary_ipv4_pub))
    conn.commit()


def main():
    zones = ZONES[:8]
    compute = googleapiclient.discovery.build('compute', 'v1')
    # stop_instances(compute, PROJECT, zones)
    start_instances(compute, PROJECT, zones)
    store_instances(compute, PROJECT, zones)


if __name__ == '__main__':
    main()
