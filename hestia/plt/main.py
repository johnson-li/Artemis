import socket
import sqlite3
from multiprocessing.pool import ThreadPool

import paramiko
from scp import SCPClient

import hestia
import hestia.experiment.main

HOST_FILE = hestia.RESOURCE_PATH + '/hosts/hosts_plt'
DB_FILE = hestia.RESOURCE_PATH + '/db/sip.db'
USER_NAME = 'goettingenple_txp1'
pool = ThreadPool(20)
SSH_CLIENTS = {}
PROGRAMME = ['direct', 'hit', 'miss', 'sid'][0]


def read(ssh_stdin):
    lines = ''
    for line in ssh_stdin:
        lines = lines + line
    return lines.strip()


def get_sid_server(host):
    ip = socket.gethostbyname(host)
    conn = sqlite3.connect(hestia.experiment.main.DB_FILE)
    c = conn.cursor()
    c.execute("select server from sip where host = '%s'" % ip)
    for line in c.fetchall():
        return line[0]
    return None


def get_ssh(host):
    if host in SSH_CLIENTS:
        return SSH_CLIENTS[host]
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=USER_NAME, timeout=10)
    SSH_CLIENTS[host] = ssh
    return ssh


def sync_files(host):
    ssh = get_ssh(host)
    execute(ssh, 'mkdir -p ~/server')
    scp = SCPClient(ssh.get_transport())
    for f in ['conduct_exp1_direct.sh', 'conduct_exp1_hit.sh', 'conduct_exp1_miss.sh', 'conduct_exp1_sid.sh']:
        scp.put(hestia.SCRIPT_PATH + '/' + f, '~/' + f)
    arch = execute(ssh, 'uname -m')
    if arch == 'x86_64':
        for f in ['client', 'simple_client']:
            scp.put(hestia.SERVER_PATH + '/' + f, '~/server/' + f)
    elif arch == 'i686':
        for f in ['client', 'simple_client']:
            scp.put(hestia.SERVER_PATH + '/i686/' + f, '~/server/' + f)
    else:
        raise Exception("Unknown arch: " + arch)


def execute(ssh, command):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    output = read(ssh_stdout)
    return output


def conduct_experiment(host):
    print('Conduct experiment with client: ' + host)
    ssh = get_ssh(host)
    sid_server = get_sid_server(host)
    if not sid_server:
        hestia.experiment.main.run(host)
        sid_server = get_sid_server(host)
    sync_files(host)
    output = execute(ssh, './conduct_exp1_%s.sh %s' % (PROGRAMME, sid_server if PROGRAMME == 'sid' else ''))
    print('Host: {}\n'.format(host) + output)


def run(host):
    try:
        conduct_experiment(host)
    except Exception as e:
        print(host + ': ' + str(e))


def main():
    lines = []
    for line in open(HOST_FILE).readlines():
        lines.append((line.strip(),))
    hestia.experiment.main.init()
    pool.starmap(run, lines)


if __name__ == '__main__':
    main()
