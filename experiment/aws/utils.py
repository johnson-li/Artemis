import json
import os
import time
from multiprocessing import Pool

import boto3

from experiment.logging import logging

logger = logging.getLogger(__name__)

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(DIR_PATH))
REGIONS = ['eu-north-1', 'us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-east-1', 'ap-south-1',
           'ap-northeast-3', 'ap-northeast-2', 'ap-northeast-1', 'ap-southeast-2', 'ap-southeast-1',
           'ap-northeast-1', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3',
           'me-south-1', 'sa-east-1']
REGIONS = ['eu-north-1', 'us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1',
           'ap-northeast-2', 'ap-northeast-1', 'ap-southeast-2', 'ap-southeast-1',
           'ap-northeast-1', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3']
#REGIONS = ['eu-north-1', 'us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-northeast-2', 'ap-northeast-1', 'ap-southeast-2', 'ap-southeast-1',
#           'ap-northeast-1', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3']
#REGIONS = ['eu-north-1', 'us-east-2', 'us-east-1', 'ap-south-1',
#           'ap-northeast-2', 'ap-northeast-1', 'ap-southeast-2', 'ap-southeast-1',
#           'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2']
# not used 'us-west-1', 'us-west-2', 'ap-east-1', 'eu-west-3', 'sa-east-1'

REFRESH = False
CONCURRENCY = 2


def start_instance(instance_id, region):
    client = boto3.client('ec2', region_name=region)
    return client.start_instances(InstanceIds=[instance_id], DryRun=False)


def stop_instance(instance_id, region):
    client = boto3.client('ec2', region_name=region)
    return client.stop_instances(InstanceIds=[instance_id], DryRun=False)


def list_instances(region):
    ec2 = boto3.resource('ec2', region_name=region)
    instances = ec2.instances.filter()
    res = []
    for instance in instances:
        if instance.state['Name'] in ['terminated', 'shutting-down']:
            continue
        res.append((instance.id, instance.state, instance.public_ip_address))
    return res


def wait_for_instance_initiation(region):
    ec2 = boto3.resource('ec2', region_name=region)
    finish = False
    while not finish:
        instances = ec2.instances.filter()
        finish = True
        for instance in instances:
            if instance.state['Name'] not in ['terminated', 'running']:
                finish = False
                time.sleep(1)
                break


def get_image_id(region):
    client = boto3.client('ec2', region_name=region)
    images = client.describe_images(Filters=[
        {
            'Name': 'architecture',
            'Values': ['x86_64']
        },
        {
            'Name': 'name',
            'Values': ['ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-2020*']
        },
    ])
    images = [(i['ImageId'], i['CreationDate'], i['Name']) for i in images['Images']]
    images = sorted(images, key=lambda a: a[1], reverse=True)
    return images[0][0]


def get_key_pair_name(region):
    client = boto3.client('ec2', region_name=region)
    key_pairs = client.describe_key_pairs()['KeyPairs']
    key = 'gcp3'
    for key_pair in key_pairs:
        if key_pair['KeyName'] == key:
            return key
    client.import_key_pair(KeyName=key, PublicKeyMaterial=open('/home/johnsonli1993/.ssh/id_rsa.pub').read().strip())
    return key


def get_instance_type(region):
    client = boto3.client('ec2', region_name=region)
    types = client.describe_instance_type_offerings()['InstanceTypeOfferings']
    types = [i['InstanceType'] for i in types]
    return 't3.micro' if 't3.micro' in types else 't2.micro'


def create_instance(region, image_id=None, instance_type=None, number=1):
    ec2 = boto3.resource('ec2', region_name=region)
    if not image_id:
        image_id = get_image_id(region=region)
    if not instance_type:
        instance_type = get_instance_type(region=region)
    instances = ec2.create_instances(
        ImageId=image_id,
        MinCount=number,
        MaxCount=number,
        InstanceType=instance_type,
        KeyName=get_key_pair_name(region=region),
        UserData=region,
    )
    init_security_groups(region=region)
    return instances


def init_security_groups(region):
    client = boto3.client('ec2', region_name=region)
    security_groups = client.describe_security_groups()['SecurityGroups']
    for security_group in security_groups:
        permissions = security_group['IpPermissions']
        permissions_okay = False
        for permission in permissions:
            ip_ranges = permission['IpRanges']
            for ip_range in ip_ranges:
                if ip_range['CidrIp'] == '0.0.0.0/0':
                    permissions_okay = True
                    break
            if permissions_okay:
                break
        if permissions_okay:
            continue
        client.authorize_security_group_ingress(GroupId=security_group['GroupId'], IpPermissions=[{
            'IpProtocol': '-1',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': '',
                },
            ],
        }])
    return security_groups


def get_instance_state():
    client = boto3.client('ec2', region_name=region)


def conduct_experiment():
    pass


def remove_instance(instance_id, region):
    client = boto3.client('ec2', region_name=region)
    return client.terminate_instances(InstanceIds=[instance_id], DryRun=False)


def run(region):
    if REFRESH:
        for instance_id, _, _ in list_instances(region=region):
            remove_instance(instance_id, region=region)
        create_instance(region=region)
        wait_for_instance_initiation(region=region)
    if len(list_instances(region=region)) == 0:
        create_instance(region=region)
        wait_for_instance_initiation(region=region)
    need_to_wait = False
    ans = []
    for instance_id, state, ip in list_instances(region=region):
        if state != 'running':
            start_instance(instance_id, region=region)
            need_to_wait = True
        ans.append((ip, region))
    if need_to_wait:
        wait_for_instance_initiation(region=region)
    return ans


def export_json(ips):
    hosts_file = os.path.join(PROJECT_PATH, 'experiment/client/data/hosts.json')
    # hosts = json.load(open(hosts_file))
    hosts = []
    for ip in ips:
        hosts.append({'hostname': ip[0], 'username': 'ubuntu', 'region': ip[1]})
    json.dump(hosts, open(hosts_file, 'w'))


def list():
    pool = Pool(CONCURRENCY)
    ans = pool.map(list_instances, REGIONS)
    l = []
    for a in ans:
        l += a
    return l


def start(start=0, end=len(REGIONS)):
    regions = REGIONS[start:end]
    pool = Pool(CONCURRENCY)
    logger.info("Conduct experiment in %d regions: %s" % (len(regions), regions))
    ans = pool.map(run, regions)
    ips = []
    for a in ans:
        ips += a
    export_json(ips)


def clean_up():
    for region in REGIONS:
        for instance_id, _, _ in list_instances(region=region):
            remove_instance(instance_id, region=region)
