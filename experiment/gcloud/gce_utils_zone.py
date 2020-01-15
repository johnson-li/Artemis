import uuid

from experiment.gcloud.constant import *
from experiment.gcloud.config import *
from experiment.gcloud.gce_utils import get_gce_client, create_instance, stop_instance, delete_instance, \
    init_experiment, init_instance, start_instance, is_hestia_project


def get_instances(zone, hestia_only=True):
    client = get_gce_client()
    result = client.instances().list(project=PROJECT_ID, zone=zone).execute()
    res = result['items'] if 'items' in result else []
    if hestia_only:
        res = list(filter(is_hestia_project, res))
    return res


def create_instances_for_zone(zone):
    return [create_instance(zone, 'hestia-%s' % str(uuid.uuid4())), ]


def stop_instances(zone, hestia_only=True):
    return [stop_instance(instance) for instance in get_instances(zone, hestia_only=hestia_only)]


def delete_instances(zone, hestia_only=True):
    return [delete_instance(instance) for instance in get_instances(zone, hestia_only=hestia_only)]


def start_instances(zone, hestia_only=True):
    return [start_instance(instance) for instance in get_instances(zone, hestia_only=hestia_only)]


def init_instances(zone, hestia_only=True):
    return [init_instance(instance) for instance in get_instances(zone, hestia_only=hestia_only)]


def init_experiments(zone, hestia_only=True):
    return [init_experiment(instance) for instance in get_instances(zone, hestia_only=hestia_only)]


def instances_started(zone):
    instances = get_instances(zone)
    return all([i['status'] == GCE_MACHINE_STATUS_RUNNING for i in instances])
