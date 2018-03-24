from multiprocessing.pool import ThreadPool
from subprocess import PIPE, run

import paramiko

from hestia import SCRIPT_PATH, RESOURCE_PATH

SCRIPT_FILE = SCRIPT_PATH + '/allNodes.sh'
HOSTS_FILE = RESOURCE_PATH + '/hosts/hosts_plt'
USER_NAME = 'goettingenple_txp1'
AVAILABLE_HOSTS = []

pool = ThreadPool(20)


def ssh_test(host):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=USER_NAME, timeout=10)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('uname -a')
        for line in ssh_stdout:
            if 'Linux' in line:
                print('Valid host: ' + host)
                AVAILABLE_HOSTS.append(host)
                break
        ssh.close()
    except Exception as e:
        print('Error: ' + str(e))


def main():
    result = run([SCRIPT_FILE], stdout=PIPE)
    hosts = []
    for line in result.stdout.decode('utf-8').split('\n'):
        if line.endswith(' boot'):
            hosts.append(line.split(' ')[1])
    pool.map(ssh_test, hosts)
    # client = ParallelSSHClient(hosts)
    # output = client.run_command('uname', user=USER_NAME)
    # for host, host_output in output.items():
    #     for line in host_output.stdout:
    #         print(line)
    #         AVAILABLE_HOSTS.append(host)
    print(AVAILABLE_HOSTS)
    with open(HOSTS_FILE, 'w') as f:
        f.writelines(AVAILABLE_HOSTS)


if __name__ == '__main__':
    main()
