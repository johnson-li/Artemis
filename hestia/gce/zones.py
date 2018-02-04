ZONES = ['us-east1-c', 'us-east4-c', 'us-central1-c', 'us-west1-c', 'europe-west4-c', 'europe-west1-c',
         'europe-west3-c', 'europe-west2-c', 'asia-east1-c', 'asia-southeast1-b', 'asia-northeast1-c', 'asia-south1-c',
         'australia-southeast1-c', 'southamerica-east1-c', 'northamerica-northeast1-c']


def shrink(name):
    return '_'.join([n[:2] for n in name.split('-')])
