import os
import time
import zipfile
import json
import paramiko

from experiment.gcloud.config import *
from experiment.gcloud.gce_utils import instances_already_created, get_instance_zone, get_external_ip
from experiment.gcloud.gce_utils_multiplexing import GceUtilMul
from experiment.gcloud.logging import logging

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CONCURRENCY = 10
zones = ZONES[:2]
restart_for_each_run = False
gce_util_mul = GceUtilMul(concurrency=CONCURRENCY, zones=zones)
logger = logging.getLogger('main')

logger.info('Concurrency: %d' % CONCURRENCY)
logger.info('Zones: %s' % str(zones))


def clean():
    gce_util_mul.delete_instances()


def get_instances():
    return gce_util_mul.get_instances()

def get_ip(instance):
    ex_ip = []
    in_ip = []
    for interface in instance['networkInterfaces']:
        for config in interface['accessConfigs']:
            if config['name'] == 'External NAT':
                ex_ip.append(config['natIP'])
        in_ip.append(interface['networkIP'])
    return ex_ip[0], in_ip[0], ex_ip[1], in_ip[1]


def get_mac(instance):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ip = get_external_ip(instance)
    key = paramiko.RSAKey.from_private_key_file('/home/wch19990119/.ssh/id_rsa')
    client.connect(hostname=ip, username='wch19990119', port=22, pkey=key, allow_agent=False, look_for_keys=False)

    name = instance['name']
    stdin, stdout, stderr = client.exec_command("cat /sys/class/net/ens4/address")
    mac1 = stdout.read().decode()[:-1]
    stdin, stdout, stderr = client.exec_command("cat /sys/class/net/ens5/address")
    mac2 = stdout.read().decode()[:-1]
    return mac1, mac2


def prepare_instances():
    instances = get_instances()
    logging.info('existing instances: %s' % [i['name'] for i in instances])

    if instances_already_created(zones, instances):
        if restart_for_each_run:
            gce_util_mul.stop_instances()
            gce_util_mul.start_instances()
            gce_util_mul.wait_for_instances_to_start()
            time.sleep(5)
    else:
        gce_util_mul.delete_instances()
        gce_util_mul.wait_for_instances_to_delete()
        gce_util_mul.create_instances()
        gce_util_mul.wait_for_instances_to_start()
        time.sleep(10)

    lis = {}
    for i in instances:
        name = i['name']
        ex_ip1, in_ip1, ex_ip2, in_ip2 = get_ip(i)
        zone = get_instance_zone(i)
        mac1, mac2 = get_mac(i)
        lis[name] = {'external_ip1': ex_ip1, 'external_ip2': ex_ip2, 'internal_ip1': in_ip1, 'internal_ip2': in_ip2, 'mac1': mac1, 'mac2': mac2, 'zone': zone}

    with open('machine.json','w',encoding='utf-8') as f:
        json.dump(lis,f,ensure_ascii=False)


    logger.info('Initiate instances')
    gce_util_mul.init_instances()
    logger.info('Initiate experiments')
    # gce_util_mul.init_experiment()


def conduct_experiment():
    pass


def zip_data():
    zipf = zipfile.ZipFile('%s/data.zip' % DIR_PATH, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk('%s/data' % DIR_PATH):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=os.path.join(root[len(DIR_PATH) + 1:], file))
    zipf.close()


def main():
    zip_data()
    # clean()
    prepare_instances()
    # conduct_experiment()


if __name__ == '__main__':
    main()
