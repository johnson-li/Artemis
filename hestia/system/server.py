import yaml

from hestia import RESOURCE_PATH


def load_server_info():
    with open(RESOURCE_PATH + "/system/instance.yaml", 'r') as stream:
        print(yaml.load(stream))


def start_servers():
    """
        Start servers in different data centers
    """
    pass


def init_servers():
    """
        Configure the servers when they are started, including NIC, IP address, etc
    """
    pass


if __name__ == '__main__':
    load_server_info()
