import googleapiclient.discovery

PROJECT = 'triton-176509'


def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']


def main():
    compute = googleapiclient.discovery.build('compute', 'v1')
    instances = list_instances(compute, PROJECT, 'us-central1-c')
    print(instances)


if __name__ == '__main__':
    main()
