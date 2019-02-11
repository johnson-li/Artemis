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


def get_server(ip):
    datacenter = get_datacenter(ip)
    candidates = list(filter(lambda x: x['phy'] == ip, datacenter['servers']))
    return candidates[0] if candidates else None


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
    for d in instances['databases']:
        if d['ip'] == ip:
            return d
    return None


def get_database(name):
    instances = load_server_info()
    for d in instances['databases']:
        if d['name'] == name:
            return d
    return None


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
        server = get_server(ip)
        info = load_server_info()
        execute(client, 'echo "DATACENTER=%s" >> ~/env ' % dc['name'])
        execute(client, 'echo "DATABASE=%s" >> ~/env ' % info['database']['ip'])
        if get_balancer(ip):
            execute(client, 'echo "interface=bridge" >> ~/env')
        else:
            execute(client, 'echo "interface=%s" >> ~/env' % server['unicast'])
            execute(client, 'echo "unicast=%s" >> ~/env' % ip)

    init_env()
    init_apt()
    init_ovs()
    init_routing()
    client.close()


def configure_db_master_slave():
    master = [d for d in load_server_info()['databases'] if d['role'] == 'master'][0]
    slaves = [d for d in load_server_info()['databases'] if d['role'] == 'slave']
    account = load_account()
    user = account['user']
    passwd = account['passwd']
    client = connect(user, passwd, master['ip'])
    execute(client, 'sudo sed -i \'/#server-id/c\\server-id = %d\' /etc/mysql/mysql.conf.d/mysqld.cnf' %
            master['server-id'])
    execute(client,
            'sudo sed -i \'/#log_bin/c\\log_bin = /var/log/mysql/mysql-bin.log\' /etc/mysql/mysql.conf.d/mysqld.cnf')
    execute(client, 'sudo sed -i \'/#binlog_do_db/c\\binlog_do_db = sid\' /etc/mysql/mysql.conf.d/mysqld.cnf')
    execute(client, 'sudo service mysql restart')
    execute(client, 'echo "GRANT REPLICATION SLAVE ON *.* TO \'slave_user\'@\'%\' IDENTIFIED BY \'password\';" |'
                    'mysql -u root -p root')
    execute(client, 'echo "GRANT ALL PRIVILEGES ON *.* TO \'johnson\'@\'%\' IDENTIFIED BY \'welcOme0!\' '
                    'WITH GRANT OPTION; FLUSH PRIVILEGES;" | mysql -u root -p root')
    execute(client, 'echo "FLUSH PRIVILEGES;" | mysql -u root -p root')
    for slave in slaves:
        client = connect(user, passwd, slave['ip'])
        execute(client, 'sudo sed -i \'/#server-id/c\\server-id = %d\' /etc/mysql/mysql.conf.d/mysqld.cnf' %
                slave['server-id'])
        execute(client, 'sudo sed -i \'/#log_bin/c\\relay-log = /var/log/mysql/mysql-relay-bin.log\n'
                        'log_bin = /var/log/mysql/mysql-bin.log\' /etc/mysql/mysql.conf.d/mysqld.cnf')
        execute(client, 'sudo sed -i \'/#binlog_do_db/c\\binlog_do_db = sid\' /etc/mysql/mysql.conf.d/mysqld.cnf')
        execute(client, 'sudo service mysql restart')
        execute(client, 'echo "STOP SLAVE IO_THREAD FOR CHANNEL \'\';" | mysql -u root -p root')
        execute(client,
                'echo "CHANGE MASTER TO MASTER_HOST=\'%s\',MASTER_USER=\'slave_user\', MASTER_PASSWORD=\'password\', '
                'MASTER_LOG_FILE=\'mysql-bin.000001\', MASTER_LOG_POS = 1;" | mysql -u root -p root' % master['ip'])
        execute(client, 'echo \'START SLAVE;\' | mysql -u root -p root')


def init_database():
    account = load_account()
    user = account['user']
    passwd = account['passwd']
    master = [d for d in load_server_info()['databases'] if d['role'] == 'master'][0]
    slaves = [d for d in load_server_info()['databases'] if d['role'] == 'slave']
    for slave in slaves:
        client = connect(user, passwd, slave['ip'])
        execute(client, 'echo "GRANT ALL PRIVILEGES ON *.* TO \'johnson\'@\'%\' IDENTIFIED BY \'welcOme0!\' '
                        'WITH GRANT OPTION; FLUSH PRIVILEGES;" | mysql -u root -p root')
        execute(client, 'sudo service mysql restart')
    mysqldb = MySQLdb.connect(host=master['ip'], user=master['username'], passwd=master['password'], db='sid')
    slave_mysqldbs = [MySQLdb.connect(s['ip'], s['username'], s['password']) for s in load_server_info()['databases'] if
                      s['role'] == 'slave']
    mysqldb.autocommit(True)
    [slave.autocommit(True) for slave in slave_mysqldbs]
    cursor = mysqldb.cursor()
    slave_cursors = [slave.cursor() for slave in slave_mysqldbs]
    cursor.execute('drop database if exists sid')
    [c.execute('drop database if exists sid') for c in slave_cursors]
    cursor.execute('create database sid')
    [c.execute('create database sid') for c in slave_cursors]
    cursor.execute('use sid')
    configure_db_master_slave()
    for f in ['init_deployment.sql', 'init_intra.sql', 'init_clients.sql', 'init_mea.sql']:
        print('execute %s' % f)
        cursor.execute(read_file(f))
    for line in read_file_lines('init.sql'):
        if line:
            cursor.execute(line)
    cursor.close()
    [c.close() for c in slave_cursors]


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
