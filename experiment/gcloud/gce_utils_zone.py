import uuid

from experiment.gcloud.config import *
from experiment.gcloud.constant import *
from experiment.gcloud.gce_utils import get_gce_client, create_instance, stop_instance, delete_instance, \
    init_experiment, init_instance, start_instance, is_hestia_project, conduct_experiment, \
    delete_client_instance


def get_instances(zone, instances=None, hestia_only=True):
    if not instances:
        client = get_gce_client()
        result = client.instances().list(project=PROJECT_ID, zone=zone).execute()
        instances = result['items'] if 'items' in result else []
        if hestia_only:
            instances = list(filter(is_hestia_project, instances))
        return instances
    res = []
    for instance in instances:
        if instance['zone'].split('/')[-1] == zone:
            res.append(instance)
    return res


def get_client_instances(zone, instances=None, hestia_only=True):
    if not instances:
        client = get_gce_client()
        result = client.instances().list(project=PROJECT_ID, zone=zone).execute()
        instances = result['items'] if 'items' in result else []
        if hestia_only:
            instances = list(filter(is_hestia_project, instances))
        return instances
    res = []
    for instance in instances:
        if instance['zone'].split('/')[-1] == zone and 'client' in instance['name']:
            res.append(instance)
    return res


def create_instances(zone):
    return [create_instance(zone, 'hestia-%s-%s' % (zone, 'router')),
            create_instance(zone, 'hestia-%s-%s' % (zone, 'server'))]


def stop_instances(zone, hestia_only=True):
    return [stop_instance(instance)
            for instance in get_instances(zone, hestia_only=hestia_only)]


def delete_instances(zone, hestia_only=True):
    return [delete_instance(instance)
            for instance in get_instances(zone, hestia_only=hestia_only)]


def delete_client_instances(zone, hestia_only=True):
    return [delete_instance(instance)
            for instance in get_client_instances(zone, hestia_only=hestia_only)]


def start_instances(zone, hestia_only=True):
    return [start_instance(instance)
            for instance in get_instances(zone, hestia_only=hestia_only)]


def init_instances(zone, execute_init_script=True, hestia_only=True):
    return [init_instance(instance, execute_init_script=execute_init_script)
            for instance in get_instances(zone, hestia_only=hestia_only)]


def init_experiments(zone, hestia_only=True):
    return [init_experiment(instance)
            for instance in get_instances(zone, hestia_only=hestia_only)]


def instances_started(zone):
    instances = get_instances(zone)
    return all([i['status'] == GCE_MACHINE_STATUS_RUNNING
                for i in instances])


def instances_deleted(zone):
    instances = get_instances(zone)
    return not instances


def conduct_experiments(zone, instances):
    return [conduct_experiment(instance) for instance
            in get_instances(zone, instances=instances, hestia_only=True)]

