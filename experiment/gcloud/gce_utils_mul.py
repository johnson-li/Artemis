from multiprocessing import Pool

from experiment.gcloud import gce_utils
from experiment.gcloud.config import *


def get_instances(concurrency=1):
    res = []
    with Pool(concurrency) as pool:
        result = pool.starmap(gce_utils.get_instances_from_zone, [(zone,) for zone in ZONES])
    for r in result:
        res.extend(r)
    res = list(filter(lambda x: x is not None, res))
    return res
