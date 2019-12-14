import json
from experiment.gcloud.gce_utils_mul import get_instances
from experiment.gcloud.gce_utils import delete_instance


def main():
    instances = get_instances(concurrency=10)
    print(json.dumps(instances, indent=2))


if __name__ == '__main__':
    main()
