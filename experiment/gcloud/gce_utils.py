import os
import json

import googleapiclient.discovery
import paramiko
from google.oauth2 import service_account

from experiment.gcloud.config import *
from experiment.gcloud.logging import logging

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
logger = logging.getLogger(__name__)


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
    for item in instance.get('metadata', {}).get('items', []):
        if item['key'] == 'hestia_exp' and item['value'] == 'true':
            return True
    return False


def create_instance(zone, name):
    client = get_gce_client()
    image_response = client.images().getFromFamily(project='gce-uefi-images', family='ubuntu-1804-lts').execute()
    source_disk_image = image_response['selfLink']
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    subnet = "regions/%s/subnetworks/default2" % zone[:-2]
    startup_script = open(os.path.join(os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    if os.path.isfile(os.path.expanduser('~/.ssh/id_rsa.pub')):
        pub = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read().strip()
        startup_script += f"\necho '{pub}' >> /home/johnsonli1993/.ssh/authorized_keys"
    config = {
        'description': '',
        'name': name,
        'machineType': machine_type,
        'disks': [{'boot': True, 'autoDelete': True, 'initializeParams': {
            'sourceImage': source_disk_image, 'diskSizeGb': 30}}],
        'networkInterfaces': [{'network': 'global/networks/default',
                              'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}]},
                              {'network': 'global/networks/default2',
                               'subnetwork': subnet,
                               'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}]},
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


def execute_ssh_sync(client, command, target_ip=None):
    stdin, stdout, stderr = client.exec_command(command)
    first_error = True
    for line in stdout:
        if line.strip('\n'):
            logger.debug(line.strip('\n'))
    for line in stderr:
        if line.strip('\n'):
            if first_error:
                logger.error("target_ip: %s, command: %s" % (target_ip, command))
                first_error = False
            logger.error(line.strip('\n'))
    exit_status = stdout.channel.recv_exit_status()
    return exit_status


##
# Transport data and install software
#
def init_instance(instance, execute_init_script=True):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ip = get_external_ip(instance)
    key = paramiko.RSAKey.from_private_key_file(os.path.expanduser('~/.ssh/id_rsa'))
    client.connect(hostname=ip, username='wch19990119', port=22, pkey=key, allow_agent=False, look_for_keys=False)
    # TODO: calculate the md5 of local data.zip and remote data.zip. Re-upload data.zip if the md5 is not matched
    stdin, stdout, stderr = client.exec_command("md5sum data.zip | cut -d ' ' -f1")
    remote_md5 = stdout.read().decode()
    s = os.popen("md5sum %s/data.zip | cut -d ' ' -f1" % DIR_PATH)
    local_md5 = s.read()
    if remote_md5 != local_md5:
        sftp = paramiko.SFTPClient.from_transport(client.get_transport())
        sftp.put('%s/data.zip' % DIR_PATH, 'data.zip')
        execute_ssh_sync(client, 'sudo DEBIAN_FRONTEND=noninteractive apt-get install -yqq unzip; '
                                 '[ -e data ] && rm -r data; '
                                 'unzip data.zip;'
                                 'cp -r data/websites ./', ip)
    f = open('machine.json', encoding='utf-8')
    lis = json.loads(f.read())
    name = instance['name']
    lis['hostname'] = name
    execute_ssh_sync(client, "echo '{}' > machine.json".format(json.dumps(lis)), ip)
    if execute_init_script:
        #command = 'sudo DEBIAN_FRONTEND=noninteractive apt-get install tmux'
        #execute_ssh_sync(client, command, ip)
        #command = "tmux ls | grep init_sh"
        #stdin, stdout, stderr = client.exec_command(command)
        #command = "tmux new -d -s init_sh"
        #stdout = stdout.read().decode()
        #if stdout=='':
        #    execute_ssh_sync(client, command, ip)
        #command = "tmux send -t init_sh 'chmod +x data/init.sh && ./data/init.sh' ENTER"
        #execute_ssh_sync(client, command, ip)
        execute_ssh_sync(client, 'chmod +x data/init_wrapper.sh && ./data/init_wrapper.sh', ip)
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


def conduct_experiment(instance):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ip = get_external_ip(instance)
    key = paramiko.RSAKey.from_private_key_file(os.path.expanduser('~/.ssh/id_rsa'))
    client.connect(hostname=ip, username='wch19990119', port=22, pkey=key, allow_agent=False, look_for_keys=False)
    execute_ssh_sync(client, 'chmod +x data/start_experiment.sh && ./data/start_experiment.sh', ip)

