from multiprocessing import Pool

from experiment.gcloud import gce_utils
from experiment.gcloud.config import *


class GceUtilMul(object):
    def __init__(self, concurrency=1, zones=ZONES):
        self.concurrency = concurrency
        self.zones = zones

    def get_instances(self):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils.get_instances_from_zone, [(zone,) for zone in self.zones])
            res = list(filter(lambda x: x is not None, result))
            return res

    def create_instances(self):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils.create_instance,
                                  [(zone, 'machine in $s'.format(zone)) for zone in self.zones])
            res = list(filter(lambda x: x is not None, result))
            return res

    ##
    # Delete virtual machines
    #
    def delete_instances(self):
        with Pool(self.concurrency) as pool:
            result = pool.starmap(gce_utils.get_instances_from_zone, [(zone,) for zone in self.zones])
            res = list(filter(lambda x: x is not None, result))
            return res

    ##
    # Stop virtual machines
    #
    def stop_instances(self):
        pass

    ##
    # Start virtual machines
    #
    def start_instances(self):
        pass

    ##
    # Check if software is all installed and install it if not
    #
    def init_instances(self):
        pass

    ##
    # Prepare environments for experiment
    #
    def init_experiment(self):
        pass

    ##
    # Wait for previous operations to finish
    #
    def wait_for_processing(self):
        pass
