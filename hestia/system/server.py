from multiprocessing import Pool

import paramiko
import yaml

from hestia import RESOURCE_PATH
from hestia.system.main import logging


def read_file(path):
    with open(RESOURCE_PATH + '/system/%s' % path, 'r') as stream:
        return ' '.join([line.strip() for line in stream.readlines()])


def read_file_lines(path):
    with open(RESOURCE_PATH + '/system/%s' % path, 'r') as stream:
        return [line.strip() for line in stream.readlines()]


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
    client.exec_command("echo `date` '%s' >> ~/hestia.log" % cmd)
    stdin, stdout, stderr = client.exec_command(cmd)
    result_code = stdout.channel.recv_exit_status()
    if result_code != 0:
        logging.warning('[%s] %s' % (client.get_transport().sock.getpeername()[0], cmd))
        for line in stderr:
            if line.strip():
                logging.warning('[%s] %s' % (client.get_transport().sock.getpeername()[0], line.strip()))
        for line in stdout:
            if line.strip():
                logging.warning('[%s] %s' % (client.get_transport().sock.getpeername()[0], line.strip()))
    return result_code == 0


def get_datacenter(ip):
    instances = load_server_info()
    for datacenter in instances['datacenters']:
        if ip in datacenter['loadbalancers'] or ip in datacenter['servers']:
            return datacenter


def is_balancer(ip):
    datacenter = get_datacenter(ip)
    return ip in datacenter['loadbalancers']


def init_system(user, passwd, ip):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.get_transport()
    client.connect(ip, username=user, password=passwd)
    logging.debug("connected to: " + ip)
    config = load_config()

    # apt install
    def init_apt():
        role = 'balancer' if is_balancer(ip) else 'server'
        prefixes = ['all', role]
        [[execute(client, cmd) for cmd in config[prefix]['pre']] for prefix in prefixes if config[prefix]['pre']]
        [execute(client, 'sudo apt install -yq %s' % ' '.join(config[prefix]['apt'])) for prefix in prefixes if
         config[prefix]['apt']]
        [[execute(client, cmd) for cmd in config[prefix]['post']] for prefix in prefixes if config[prefix]['post']]

    # gre tunnels
    def init_ovs():
        execute(client, """
                for bridge in `sudo ovs-vsctl show| grep Bridge| sed -E 's/ +Bridge //'| sed -E 's/"//g'`; 
                do sudo ovs-vsctl del-br $bridge; 
                done
        """)
        datacenter = get_datacenter(ip)
        if is_balancer(ip):
            # cross balancer tunnel
            for index, dc in enumerate(load_server_info()['datacenters']):
                if dc != datacenter:
                    execute(client, 'sudo ovs-vsctl add-br balancer%d; sudo ovs-vsctl add-port balancer%d tunnel%d -- '
                                    'set interface tunnel%d type=gre, options:remote_ip=%s' %
                            (index, index, index + 1000, index + 1000, dc['loadbalaners'][0]))
            # balancer to server tunnel
            for index, server in enumerate(datacenter['servers']):
                execute(client, 'sudo ovs-vsctl add-br server%d; sudo ovs-vsctl add-port server%d tunnel%d -- '
                                'set interface tunnel%d type=gre, options:remote_ip=%s' %
                        (index, index, index, index, server))
                execute(client, 'sudo ovs-ofctl del-flows server%d' % index)
                execute(client,
                        'sudo ovs-ofctl add-flow server%d in_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface tunnel%d| tail -n1| egrep -o "[0-9]+"`,actions=local' % (
                            index, index))
                execute(client,
                        'sudo ovs-ofctl add-flow server%d in_port=local,actions=`sudo ovs-vsctl -- --columns=name,ofport list Interface tunnel%d| tail -n1| egrep -o "[0-9]+"`' % (
                            index, index))
        else:
            # server to balancer tunnel
            for index, balancer in enumerate(datacenter['loadbalancers']):
                execute(client, 'sudo ovs-vsctl add-br balancer%d; sudo ovs-vsctl add-port balancer%d tunnel%d -- '
                                'set interface tunnel%d type=gre, options:remote_ip=%s' %
                        (index, index, index, index, balancer))
                execute(client, 'sudo ifconfig balancer%d %s/32 up' % (index, balancer))

    # delete content and create tables
    def init_db():
        if is_balancer(ip):
            execute(client, 'echo drop database sid if exists| mysql -uroot --password=root')
            execute(client, 'echo create database sid | mysql -uroot --password=root')
            execute(client, 'mysql -uroot --password=root sid -e "%s"' % read_file('init_inter.sql'))
            execute(client, 'mysql -uroot --password=root sid -e "%s"' % read_file('init_intra.sql'))
            for line in read_file_lines('init.sql'):
                execute(client, 'mysql -uroot --password=root sid -e "%s"' % line)

    init_apt()
    init_ovs()
    init_db()


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
