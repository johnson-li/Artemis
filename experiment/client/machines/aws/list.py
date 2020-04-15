from experiment.aws.utils import list_instances


def main():
    instances = list_instances()
    print(instances)


if __name__ == '__main__':
    main()
