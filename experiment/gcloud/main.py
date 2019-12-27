from experiment.gcloud.config import *
from experiment.gcloud.gce_utils_mul import GceUtilMul
from experiment.gcloud.gce_utils import instances_already_created

CONCURRENCY = 10
zones = ZONES[:1]
gce_util_mul = GceUtilMul(concurrency=CONCURRENCY, zones=zones)


def prepare_instances():
    instances = gce_util_mul.get_instances()
    if instances_already_created(instances):
        gce_util_mul.stop_instances()
        gce_util_mul.start_instances()
    else:
        gce_util_mul.delete_instances()
        gce_util_mul.create_instances()
    gce_util_mul.init_instances()
    gce_util_mul.init_experiment()


def conduct_experiment():
    pass


def main():
    prepare_instances()
    conduct_experiment()


if __name__ == '__main__':
    main()
