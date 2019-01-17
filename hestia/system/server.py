from multiprocessing import Pool

import MySQLdb
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
        ips += [b['phy'] for b in datacenter['loadbalancers']]
        ips += [s['phy'] for s in datacenter['servers']]
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
        if ip in [b['phy'] for b in datacenter['loadbalancers']] or ip in [s['phy'] for s in datacenter['servers']]:
            return datacenter


def get_balancer(ip):
    datacenter = get_datacenter(ip)
    candidates = list(filter(lambda x: x['phy'] == ip, datacenter['loadbalancers']))
    return candidates[0] if candidates else None


def sid(ip):
    datacenter = get_datacenter(ip)
    return [b['sid'] for b in datacenter['loadbalancers'] if b['phy'] == ip][0]


def is_server(ip):
    datacenter = get_datacenter(ip)
    return ip in [b['phy'] for b in datacenter['servers']]


def is_database(ip):
    instances = load_server_info()
    return ip == instances['database']['ip']


def connect(user, passwd, ip):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.get_transport()
    client.connect(ip, username=user, password=passwd)
    logging.debug("connected to: " + ip)
    return client


def router(ip):
    return '.'.join(ip.split('.')[:3]) + '.1'


def init_system(user, passwd, ip):
    client = connect(user, passwd, ip)
    config = load_config()

    # apt install
    def init_apt():
        role = 'balancer' if get_balancer(ip) else 'server'
        prefixes = ['all', role]
        [[execute(client, cmd) for cmd in config[prefix]['pre']] for prefix in prefixes if config[prefix]['pre']]
        [execute(client, 'sudo apt install -yq %s' % ' '.join(config[prefix]['apt'])) for prefix in prefixes if
         config[prefix]['apt']]
        [[execute(client, cmd) for cmd in config[prefix]['post']] for prefix in prefixes if config[prefix]['post']]

    # gre tunnels
    def init_ovs():
        execute(client, "sudo iptables -I OUTPUT -p icmp --icmp-type destination-unreachable -j DROP")
        execute(client, """
                for bridge in `sudo ovs-vsctl show| grep Bridge| sed -E 's/ +Bridge //'| sed -E 's/"//g'`; 
                    do sudo ovs-vsctl del-br $bridge; 
                done
        """)
        datacenter = get_datacenter(ip)
        if get_balancer(ip):
            balancer = get_balancer(ip)
            execute(client,
                    'sudo ovs-vsctl add-br bridge; sudo ovs-vsctl add-port bridge %s; sudo ovs-ofctl del-flows bridge' %
                    balancer['anycast'])
            execute(client, 'sudo ifconfig bridge %s/24 up' % balancer['sid'])
            query_port = '`sudo ovs-vsctl -- --columns=name,ofport list Interface %s| tail -n1| egrep -o "[0-9]+"`'
            query_router_mac = '`ping -c1 %s > /dev/null; arp| grep "%s "| egrep -o "[0-9a-z:]{12,}"`'
            execute(client,
                    'sudo ovs-ofctl add-flow bridge in_port=local,actions=%s' % (query_port % balancer['anycast']))
            execute(client,
                    'sudo ovs-ofctl add-flow bridge in_port=%s,actions=local' % (query_port % balancer['anycast']))
            execute(client, 'sudo ifconfig %s 0' % balancer['anycast'])
            # execute(client, 'sudo ip route add default via %s dev ac tab 1' % router(balancer['sid']))
            # execute(client, 'sudo ip rule add from %s/32 tab 1 priority 500' % balancer['sid'])
            # cross balancer tunnel
            for index, dc in enumerate(load_server_info()['datacenters']):
                if dc != datacenter:
                    remote = dc['loadbalancers'][0]
                    remote_name = remote['name']
                    execute(client,
                            'sudo ovs-vsctl add-port bridge %s -- set interface %s type=internal' % (
                                remote_name, remote_name))
                    execute(client, 'sudo ovs-vsctl add-port bridge t%s -- '
                                    'set interface t%s type=gre, options:remote_ip=%s' % (
                                remote_name, remote_name, remote['phy']))
                    execute(client, 'sudo ifconfig %s 12.12.12.12/32 up' % remote_name)
                    execute(client, 'sudo ovs-ofctl add-flow bridge in_port=%s,actions=%s' % (
                        query_port % 't%s' % remote_name, query_port % remote_name))
                    execute(client, 'sudo ovs-ofctl add-flow bridge in_port=%s,actions=%s' % (
                        query_port % remote_name, query_port % 't%s' % remote_name))
            # balancer to server tunnel
            for server in datacenter['servers']:
                server_name = server['name']
                execute(client, 'sudo ovs-vsctl add-port bridge %s -- set interface %s type=internal' % (
                    server_name, server_name))
                execute(client,
                        'sudo ovs-vsctl add-port bridge t%s -- set interface t%s type=gre, options:remote_ip=%s' % (
                            server_name, server_name, server['phy']))
                execute(client, 'sudo ifconfig %s 12.12.12.12/32 up' % server['name'])
                execute(client,
                        'sudo ovs-ofctl add-flow bridge in_port=%s,actions=mod_dl_dst:%s,%s' % (
                            query_port % 't%s' % server_name,
                            query_router_mac % (router(balancer['sid']), router(balancer['sid'])),
                            query_port % balancer['anycast']))
                execute(client,
                        'sudo ovs-ofctl add-flow bridge in_port=%s,actions=%s' % (
                            query_port % server['name'], query_port % 't%s' % server['name']))
        else:
            # server to balancer tunnel
            query_mac = '`ifconfig %s|grep HWaddr| egrep -o "[0-9a-z:]{12,}"`'
            for balancer in datacenter['loadbalancers']:
                execute(client, 'sudo ovs-vsctl add-br %s; sudo ovs-vsctl add-port %s tunnel%s -- '
                                'set interface tunnel%s type=gre, options:remote_ip=%s' %
                        (balancer['name'], balancer['name'], balancer['name'][2:], balancer['name'][2:],
                         balancer['phy']))
                execute(client, 'sudo ifconfig %s %s/32 up' % (balancer['name'], balancer['sid']))
                execute(client, 'sudo ovs-ofctl del-flows %s' % balancer['name'])
                execute(client,
                        'sudo ovs-ofctl add-flow %s in_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface tunnel%s| tail -n1| egrep -o "[0-9]+"`,actions=mod_dl_dst:%s,local' % (
                            balancer['name'], balancer['name'][2:], query_mac % balancer['name']))
                execute(client,
                        'sudo ovs-ofctl add-flow %s in_port=local,actions=`sudo ovs-vsctl -- --columns=name,ofport list Interface tunnel%s| tail -n1| egrep -o "[0-9]+"`' % (
                            balancer['name'], balancer['name'][2:]))

    def init_routing():
        if get_balancer(ip):
            datacenter = get_datacenter(ip)
            for server in datacenter['servers']:
                execute(client, 'sudo arp -s %s 00:00:00:00:00:00 -i %s' % (sid(ip), server['name']))
        if is_server(ip):
            datacenter = get_datacenter(ip)
            for index, balancer in enumerate(datacenter['loadbalancers']):
                execute(client, 'sudo arp -s %s 00:00:00:00:00:00 -i %s' % (ip, balancer['name']))
                execute(client,
                        'sudo ip route add default via %s dev %s tab %d' % (
                            balancer['sid'], balancer['name'], index + 1))
                execute(client, 'sudo ip rule add from %s/32 tab %d priority 600' % (balancer['sid'], index + 1))

    def init_env():
        dc = get_datacenter(ip)
        info = load_server_info()
        execute(client, 'echo "DATACENTER=%s" >> ~/env ' % dc['name'])
        execute(client, 'echo "DATABASE=%s" >> ~/env ' % info['database']['ip'])
        if get_balancer(ip):
            execute(client, 'echo "interface=bridge" >> ~/env')
        else:
            execute(client, 'echo "unicast=%s" >> ~/env' % ip)

    init_env()
    init_apt()
    init_ovs()
    init_routing()
    client.close()


def init_database():
    db = load_server_info()['database']
    ip = db['ip']
    user = db['username']
    passwd = db['password']
    mysqldb = MySQLdb.connect(host=ip, user=user, passwd=passwd, db='sid')
    mysqldb.autocommit(True)
    cursor = mysqldb.cursor()
    cursor.execute('drop database if exists sid')
    cursor.execute('create database sid')
    cursor.execute('use sid')
    for f in ['init_deployment.sql', 'init_intra.sql', 'init_clients.sql', 'init_mea.sql']:
        print('execute %s' % f)
        cursor.execute(read_file(f))
    for line in read_file_lines('init.sql'):
        if line:
            cursor.execute(line)
    cursor.close()


def init_systems():
    """
        Install initial software and configure them. Get the application code.
    """
    ips = load_server_ips()
    account = load_account()
    init_database()
    with Pool() as pool:
        pool.starmap(init_system, [(account['user'], account['passwd'], ip) for ip in ips])


def start_application(user, passwd, ip):
    client = connect(user, passwd, ip)
    config = load_config()
    execute(client, '~/app/scripts/start.sh')


def start_applications():
    """
        Run application code
    """
    ips = load_server_ips()
    account = load_account()
    with Pool() as pool:
        pool.starmap(start_application, [(account['user'], account['passwd'], ip) for ip in ips])
