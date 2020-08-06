import time
from multiprocessing import Pool

from experiment.gcloud import gce_utils_zone
from experiment.gcloud import gce_utils
from experiment.gcloud.config import *
from experiment.gcloud.logging import logging

logger = logging.getLogger(__name__)


def combine_result_list(value):
    res = []
    for v in value:
        for vv in v:
            res.append(vv)
    return res


class GceUtilMul(object):
    def __init__(self, concurrency=1, zones=ZONES):
        self.concurrency = concurrency
        self.zones = zones

    def get_instances(self):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils_zone.get_instances, [(zone,) for zone in self.zones])
            return combine_result_list(result)

    def create_instances(self, single=False):
        existing_instance = self.get_instances()
        logger.info(f'Existing instances: {existing_instance}')
        with Pool(self.concurrency) as pool:
            lis = []
            for zone in self.zones:
                if not single:
                    lis.append((zone, 'hestia-%s-%s' % (zone, 'router')))
                lis.append((zone, 'hestia-%s-%s' % (zone, 'server')))
            result = pool.starmap(gce_utils.create_instance, lis)
            return combine_result_list(result)

    def create_unboot_instances(self):
        with Pool(self.concurrency) as pool:
            lis = []
            for zone in self.zones:
                lis.append((zone, 'hestia-%s-%s' % (zone, 'router')))
                lis.append((zone, 'hestia-%s-%s' % (zone, 'server')))
            result = pool.starmap(gce_utils.create_instance, lis)
            return combine_result_list(result)

    def delete_instances(self):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils_zone.delete_instances, [(zone,) for zone in self.zones])
            return combine_result_list(result)

    def delete_client_instances(self, client_zone):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils_zone.delete_client_instances, [(zone,) for zone in client_zone])
            return combine_result_list(result)

    def stop_instances(self):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils_zone.stop_instances, [(zone,) for zone in self.zones])
            return combine_result_list(result)

    def start_instances(self):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils_zone.start_instances, [(zone,) for zone in self.zones])
            res = list(filter(lambda x: x is not None, result))
            return res

    def init_instances(self, execute_init_script=True, second_zip=False):
        with Pool(self.concurrency) as pool:
            instances = self.get_instances()
            result = pool.starmap(gce_utils.init_instance,
                                  [(instance, execute_init_script, second_zip) for instance in instances])
            return result

    def init_experiment(self):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils_zone.init_experiment,
                                  [(zone,) for zone in self.zones])
            return combine_result_list(result)

    def instances_started(self):
        return all([gce_utils_zone.instances_started(zone)
                    for zone in self.zones])

    def instances_deleted(self):
        return all([gce_utils_zone.instances_deleted(zone)
                    for zone in self.zones])

    def client_instances_deleted(self, client_zone):
        return all([gce_utils_zone.instances_deleted(zone)
                    for zone in client_zone])

    def wait_for_instances_to_delete(self):
        logger.info('Wait for instances to be deleted')
        while not self.instances_deleted():
            time.sleep(5)
        logger.info('Instances have all been deleted')

    def wait_for_client_instances_to_delete(self, client_zone):
        logger.info('Wait for client instances to be deleted')
        while not self.client_instances_deleted(client_zone=client_zone):
            time.sleep(5)
        logger.info('Client instances have all been deleted')

    def wait_for_instances_to_start(self):
        logger.info('Wait for instances to start')
        while not self.instances_started():
            time.sleep(5)
        logger.info('Instances have all started')

    def conduct_experiment(self, instances):
        logger.info('Conduct experiment')
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils_zone.conduct_experiments, [(zone, instances, ) for zone in self.zones])
            return combine_result_list(result)

    ##
    # Wait for previous operations to finish
    #
    def wait_for_processing(self):
        pass
