import json
from multiprocessing import Pool

from experiment.gcloud import gce_utils
from .config import *


def get_instances():
    result = []
    with Pool(10) as pool:
        result = pool.starmap(gce_utils.get_instances_from_zone, [(zone, ) for zone in ZONES[:1]])
    return result


def main():
    # gce_instance = create_instance(client, ZONES[0], str(uuid.uuid4()).replace('-', ''))
    # print(json.dumps(gce_instance, indent=2))
    instances = get_instances()
    print(json.dumps(instances, indent=2))


if __name__ == '__main__':
    main()
