#!/usr/bin/env python
import os
import sqlite3
import time

import hestia.aws.utils as utils
import hestia.tools.generate_hosts
from hestia import RESOURCE_PATH, SQL_PATH
from hestia.aws.sessions import Sessions

DB_PATH = RESOURCE_PATH + '/db'
DB_FILE = DB_PATH + '/instances.db'
SQL_FILE = SQL_PATH + '/instances.sql'
INITIATED_INSTANCES = []


def start_machines(sessions):
    pending_instances = []
    pending_interfaces = []

    for session in sessions:
        print('Detach interfaces in region: ' + session.region_name)
        resource = session.resource('ec2')
        for interface in resource.network_interfaces.all():
            if interface.attachment and interface.description in ('server-eth1', 'router-eth1'):
                interface.detach()
                pending_interfaces.append(interface)

    print('Wait for interfaces')
    while pending_interfaces:
        interface = pending_interfaces.pop(0)
        interface.load()
        if interface.attachment:
            pending_interfaces.append(interface)

    for session in sessions:
        print('Start instances in region: ' + session.region_name)
        resource = session.resource('ec2')
        for instance in resource.instances.all():
            name = utils.get_instance_name(instance)
            if name in ('router', 'server'):
                instance.start()
                pending_instances.append((instance, resource, session.region_name))

    print('Wait for instances')
    while pending_instances:
        instance, resource, region_name = pending_instances.pop(0)
        instance.load()
        if instance.state['Name'] != 'running':
            pending_instances.append((instance, resource, region_name))
        else:
            print('Finish instance: {} in region: {}'.format(str(instance), region_name))
            for interface in resource.network_interfaces.all():
                if not interface.attachment and interface.description == utils.get_instance_name(instance) + '-eth1':
                    pending_interfaces.append(interface)
                    time.sleep(5)
                    interface.attach(DeviceIndex=1, InstanceId=instance.id)
                    break
            INITIATED_INSTANCES.append((instance, region_name))

    print('Wait for interfaces')
    while pending_interfaces:
        interface = pending_interfaces.pop(0)
        if not interface.attachment:
            pending_interfaces.append(interface)


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


def store_instances_info():
    print('Store instances info')
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    for instance, region_name in INITIATED_INSTANCES:
        instance.load()
        try:
            for interface in instance.network_interfaces:
                if interface.attachment['DeviceIndex'] == 0:
                    primary_ipv4 = interface.private_ip_address
                    primary_ipv4_pub = interface.private_ip_addresses[0]['Association']['PublicIp']
                    primary_ipv6 = interface.ipv6_addresses[0]['Ipv6Address']
                else:
                    secondary_ipv4 = interface.private_ip_address
                    secondary_ipv4_pub = interface.private_ip_addresses[0]['Association'][
                        'PublicIp'] if utils.get_instance_name(instance) == 'router' else ''
                    secondary_ipv6 = interface.ipv6_addresses[0]['Ipv6Address']
            c.execute(
                "INSERT INTO instances (region, name, instanceId, "
                "primaryIpv4, primaryIpv6, primaryIpv4Pub, secondaryIpv4, secondaryIpv6, secondaryIpv4Pub) "
                "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                    region_name, utils.get_instance_name(instance),
                    instance.id, primary_ipv4, primary_ipv6, primary_ipv4_pub, secondary_ipv4, secondary_ipv6,
                    secondary_ipv4_pub))
        except Exception as e:
            print('Error occurred while processing instance: ' + str(instance) + ' in region: ' + region_name)
            print(e)
    conn.commit()


def allocate_ips(sessions):
    print('Allocate IPs')
    for session in sessions:
        ec2 = session.client('ec2')
        resource = session.resource('ec2')
        addresses = []
        for i in range(3):
            addresses.append(ec2.allocate_address(Domain='vpc'))
        for interface in resource.network_interfaces.all():
            if interface.description == 'server-eth0':
                ec2.associate_address(AllocationId=addresses[0]['AllocationId'], NetworkInterfaceId=interface.id)
            elif interface.description == 'router-eth0':
                ec2.associate_address(AllocationId=addresses[1]['AllocationId'], NetworkInterfaceId=interface.id)
            elif interface.description == 'router-eth1':
                ec2.associate_address(AllocationId=addresses[2]['AllocationId'], NetworkInterfaceId=interface.id)


def main():
    sessions = Sessions()
    session_list = [sessions.ap_northeast_1, sessions.ap_southeast_2, sessions.ap_southeast_1]
    # session_list = [sessions.ap_southeast_1]
    allocate_ips(session_list)
    init_db()
    start_machines(session_list)
    store_instances_info()
    hestia.tools.generate_hosts.main()


if __name__ == '__main__':
    main()
