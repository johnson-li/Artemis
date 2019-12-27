import os
from functools import lru_cache

import googleapiclient.discovery
from google.oauth2 import service_account

from experiment.gcloud.config import *


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


def is_hestia_project(instance):
    for item in instance['metadata']['items']:
        if item['key'] == 'hestia_exp' and item['value'] == 'true':
            return True
    return False


def get_instances_from_zone(zone, hestia_only=True):
    client = get_gce_client()
    result = client.instances().list(project=PROJECT_ID, zone=zone).execute()
    res = result['items'] if 'items' in result else []
    if hestia_only:
        res = list(filter(is_hestia_project, res))
    return res


def create_instance(zone, name):
    client = get_gce_client()
    image_response = client.images().getFromFamily(project='gce-uefi-images', family='ubuntu-1804-lts').execute()
    source_disk_image = image_response['selfLink']
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    startup_script = open(os.path.join(os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    config = {
        'description': '',
        'name': name,
        'machineType': machine_type,
        'disks': [{'boot': True, 'autoDelete': True, 'initializeParams': {
            'sourceImage': source_disk_image, 'diskSizeGb': 30}}],
        'networkInterfaces': [{'network': 'global/networks/default',
                               'accessConfigs': [{'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}]}],
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


def stop_instance(zone):
    pass


def start_instance(zone):
    pass


def init_instance():
    pass


def init_experiment():
    pass


def instances_already_created(instances):
    return False


