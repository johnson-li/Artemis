from multiprocessing import Pool

import paramiko
import yaml

from hestia import RESOURCE_PATH
from hestia.system.main import logging


def load_config():
    with open(RESOURCE_PATH + "/system/remote-config.yaml", 'r') as stream:
        return yaml.load(stream)


def load_server_info():
    with open(RESOURCE_PATH + "/system/instances.yaml", 'r') as stream:
        return yaml.load(stream)


def load_account():
    instances = load_server_info()
    return {'user': instances['username'], 'passwd': instances['password']}


def load_server_ips():
    instances = load_server_info()
    ips = []
    for datacenter in instances['datacenters']:
        ips += datacenter['loadbalancers']
        ips += datacenter['servers']
    return ips


def start_servers():
    """
        Start servers in different data centers
    """
    pass


def init_server(user, passwd, ip):
    pass


def init_servers():
    """
        Configure the servers when they are started, including NIC, IP address, etc
    """
    pass


def execute(client, cmd):
    stdin, stdout, stderr = client.exec_command(cmd)
    result_code = stdout.channel.recv_exit_status()
    if result_code != 0:
        for line in stderr:
            if line.strip():
                logging.warning('[%s] %s' % (ip, line.strip()))
        for line in stdout:
            if line.strip():
                logging.debug('[%s] %s' % (ip, line.strip()))
    return result_code == 0


def init_system(user, passwd, ip):
    # client = paramiko.SSHClient()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    config = load_config()
    execute(client, 'sudo apt install -yq %s' % ' '.join(config['apt']))


def init_systems():
    """
        Install initial software and configure them. Get the application code.
    """
    ips = load_server_ips()
    account = load_account()
    with Pool() as pool:
        pool.starmap(init_system, [(account['user'], account['passwd'], ip) for ip in ips])


def start_applications():
    """
        Run application code
    """
    pass
