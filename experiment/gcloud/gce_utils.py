import os
from functools import lru_cache

import googleapiclient.discovery
import paramiko
from google.oauth2 import service_account

from experiment.gcloud.config import *
from experiment.gcloud.logging import logging

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
logger = logging.getLogger(__name__)


@lru_cache()
def get_gce_client():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    delegated_credentials = credentials.with_subject(PROJECT_EMAIL)
    compute = googleapiclient.discovery.build('compute', 'v1', credentials=delegated_credentials)
    return compute


def delete_instance(instance):
    client = get_gce_client()
    res = client.instances().delete(project=PROJECT_ID, zone=instance['zone'].split('/')[-1],
                                    instance=instance['name']).execute()
    return res


def get_external_ip(instance):
    for interface in instance['networkInterfaces']:
        for config in interface['accessConfigs']:
            if config['name'] == 'External NAT':
                return config['natIP']


def is_hestia_project(instance):
    for item in instance['metadata']['items']:
        if item['key'] == 'hestia_exp' and item['value'] == 'true':
            return True
    return False


def create_instance(zone, name):
    client = get_gce_client()
    image_response = client.images().getFromFamily(project='gce-uefi-images', family='ubuntu-1804-lts').execute()
    source_disk_image = image_response['selfLink']
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    startup_script = open(os.path.join(os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    if os.path.isfile(os.path.expanduser('~/.ssh/id_rsa.pub')):
        startup_script = '%s\necho %s >> /home/johnsonli1993/.ssh/authorized_keys' \
                         % (startup_script, open(os.path.expanduser('~/.ssh/id_rsa.pub')).read())
    config = {
        'description': '',
        'name': name,
        'machineType': machine_type,
        'disks': [{'boot': True, 'autoDelete': True, 'initializeParams': {
            'sourceImage': source_disk_image, 'diskSizeGb': 30}}],
        'networkInterfaces': [{'network': 'global/networks/default',
                               'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}]},
                              # TODO: assign a second interface
                              # {'network': 'global/networks/default2',
                              #  'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}]},
                              ],
        'serviceAccounts': [{
            'email': PROJECT_EMAIL,
            'scopes': [
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring.write",
                "https://www.googleapis.com/auth/servicecontrol",
                "https://www.googleapis.com/auth/service.management.readonly",
                "https://www.googleapis.com/auth/trace.append"
            ]
        }],
        'metadata': {
            'items': [{
                'key': 'startup-script',
                'value': startup_script
            }, {
                'key': "ssh-keys",
                'value': SSH_PUBLIC_KEY
            }, {
                'key': 'hestia_exp',
                'value': 'true',
            }]
        },
    }
    gce_instance = client.instances().insert(project=PROJECT_ID, zone=zone, body=config).execute()
    return gce_instance


def stop_instance(instance):
    client = get_gce_client()
    res = client.instances().stop(project=PROJECT_ID, zone=instance['zone'].split('/')[-1],
                                  instance=instance['name']).execute()
    return res


def start_instance(instance):
    client = get_gce_client()
    res = client.instances().start(project=PROJECT_ID, zone=instance['zone'].split('/')[-1],
                                   instance=instance['name']).execute()
    return res


def execute_ssh_sync(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    for line in stdout:
        if line.strip('\n'):
            logger.debug(line.strip('\n'))
    for line in stderr:
        if line.strip('\n'):
            logger.error(line.strip('\n'))
    exit_status = stdout.channel.recv_exit_status()
    return exit_status


##
# Transport data and install software
#
def init_instance(instance):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ip = get_external_ip(instance)
    client.connect(ip, username=DEFAULT_USER_NAME)
    # TODO: calculate the md5 of local data.zip and remote data.zip. Re-upload data.zip if the md5 is not matched
    remote_md5 = 'a'
    local_md5 = 'b'
    if remote_md5 != local_md5:
        sftp = paramiko.SFTPClient.from_transport(client.get_transport())
        sftp.put('%s/data.zip' % DIR_PATH, 'data.zip')
        execute_ssh_sync(client, 'sudo apt-get install -yqq unzip; '
                                 '[ -e data ] && rm -r data; '
                                 'unzip data.zip')
    execute_ssh_sync(client, 'chmod +x data/init.sh && ./data/init.sh')
    client.close()


##
# Configure environment
#
def init_experiment(instance):
    raise NotImplementedError()


def get_instance_zone(instance):
    return instance['zone'].split('/')[-1]


def instances_already_created(zones: list, instances):
    to_be_deleted = []
    left = zones.copy()
    for zone in set([get_instance_zone(i) for i in instances]):
        if zone in left:
            left.remove(zone)
        else:
            to_be_deleted.append(zone)
    return len(left) == 0 and len(to_be_deleted) == 0
