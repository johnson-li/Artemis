from experiment.gcloud.gce_utils import create_instance, ZONES

ZONES_ALL = ['us-east1-c', 'us-east4-c', 'us-central1-c', 'us-west1-c', 'us-west2-c', 'us-west3-c',
             'europe-west1-c', 'europe-west2-c', 'europe-west3-c', 'europe-west4-c', 'europe-west6-c',
             'europe-north1-c',
             'asia-east1-c', 'asia-east2-c', 'asia-southeast1-c', 'asia-northeast1-c', 'asia-northeast2-c',
             'asia-northeast3-c', 'asia-south1-c', 'australia-southeast1-c',
             'southamerica-east1-c', 'northamerica-northeast1-c']

zones = []
for z in ZONES_ALL:
    if z not in ZONES:
        zones.append(z)

print(zones)
zones = ['southamerica-east1-c']


def main():
    print('Zones: %s' % zones)
    instances = []
    for zone in zones:
        instances.append(create_instance(zone, 'client-%s' % zone))
    print(instances)


if __name__ == '__main__':
    main()
