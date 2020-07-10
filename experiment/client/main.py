import json
import os
import subprocess
import zipfile
from shutil import copyfile,copytree

import paramiko

from experiment.gcloud.logging import logging

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(DIR_PATH))
HOSTS_PATH = os.path.join(DIR_PATH, "data/hosts.json")
REMOTE_PROJECT_PATH = '/tmp/hestia'
DATA_PATH = os.path.join(DIR_PATH, 'data')
DATA_ZIP_PATH = os.path.join(DIR_PATH, 'data.zip')
logger = logging.getLogger(__name__)

# cmd = 'lb_list=$(gcloud compute addresses list); lb_list=${lb_list#*ipv4}; lb_list=${lb_list%%EX*}; lb_ip=`echo $lb_list | sed \'s/ //g\'`; echo $lb_ip'
cmd = 'gcloud compute addresses list| grep load-balancer| egrep -o "[0-9.]{4,}"'
output, _ = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE).communicate()
lb_ip = output.decode("utf-8").strip()


def zip_data():
    WORKSPACE_PATH = os.path.dirname(PROJECT_PATH)
    copyfile('%s/machine.json' % PROJECT_PATH, '%s/data/machine.json' % DIR_PATH)
    copyfile('%s/ngtcp2/examples/client' % WORKSPACE_PATH, '%s/data/client' % DIR_PATH)
#    copyfile('%s/ngtcp2/lib/.libs/libngtcp2.so.0' % WORKSPACE_PATH, '%s/data/libngtcp2.so.0' % DIR_PATH)
    copyfile('%s/openssl/libssl.so.1.1' % WORKSPACE_PATH, '%s/data/libssl.so.1.1' % DIR_PATH)
    copyfile('%s/openssl/libcrypto.so.1.1' % WORKSPACE_PATH, '%s/data/libcrypto.so.1.1' % DIR_PATH)
    copyfile('%s/ngtcp2/index.csv' % WORKSPACE_PATH, '%s/data/index.csv' % DIR_PATH)
    copytree('%s/ngtcp2/websites' % WORKSPACE_PATH, '%s/data/websites' % DIR_PATH)
    zipf = zipfile.ZipFile(DATA_ZIP_PATH, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(DATA_PATH):
        for file in files:
            zipf.write(os.path.join(root, file),
                       arcname=os.path.join(root[len(DIR_PATH) + 1:], file))
    zipf.close()


def execute_ssh_sync(client, command):
    stdin, stdout, stderr = client.exec_command(command, timeout=30)
    first_error = True
    for line in stdout:
        if line.strip('\n'):
            logger.debug(line.strip('\n'))
    for line in stderr:
        if line.strip('\n'):
            if first_error:
                logger.error("command: %s" % command)
                first_error = False
            logger.error(line.strip('\n'))
    exit_status = stdout.channel.recv_exit_status()
    return exit_status


def conduct_experiment(hostname, username, password, region):
    logger.info('Conduct experiment on %s' % hostname)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password,
                   pkey=paramiko.RSAKey.from_private_key_file("/home/wch19990119/.ssh/id_rsa"))
    execute_ssh_sync(client, 'mkdir -p %s' % REMOTE_PROJECT_PATH)
    remote_md5 = 'a'
    local_md5 = 'b'
    if remote_md5 != local_md5:
        sftp = paramiko.SFTPClient.from_transport(client.get_transport())
        sftp.put(DATA_ZIP_PATH, '%s/data.zip' % REMOTE_PROJECT_PATH)
        execute_ssh_sync(client,
                         'sudo DEBIAN_FRONTEND=noninteractive apt-get install -yqq unzip; ' +
                         'cd %s; ' % REMOTE_PROJECT_PATH +
                         '[ -e data  ] && rm -r data; ' +
                         'unzip data.zip')
    execute_ssh_sync(client,
                     'curl -O https://lexbor.com/keys/lexbor_signing.key;' +
                     'sudo apt-key add lexbor_signing.key;' +
                     'sudo sh -c \'echo "deb https://packages.lexbor.com/ubuntu/ bionic liblexbor" > /etc/apt/sources.list.d/lexbor.list\';' +
                     'sudo sh -c \'echo "deb-src https://packages.lexbor.com/ubuntu/ bionic liblexbor" >> /etc/apt/sources.list.d/lexbor.list\';' +
                     'sudo apt-get update;' +
                     'sudo apt-get install liblexbor;' +
                     'sudo apt-get install liblexbor-dev;')

    experiment_script = '%s/data/start_wrapper.sh' % REMOTE_PROJECT_PATH
    command = 'export region=%s; export lb_ip=%s; chmod +x %s && %s' % (
        region, lb_ip, experiment_script, experiment_script)
    execute_ssh_sync(client, command)



def get_datacenters():
    data = json.load(open(os.path.join(DIR_PATH, "../../machine.json")))
    prefix = set([d[:-7] for d in data.keys() if d.startswith('hestia')])
    ans = ['%s %s %s' % (p[7:], data['%s-router' % p]['external_ip1'], data['%s-server' % p]['external_ip1'])
           for p in prefix]
    # ans = ['%s %s' % (i[7:-7], data[i]['external_ip1'])
    #        for i in data.keys() if i.endswith('router')]
    with open(os.path.join(DATA_PATH, 'datacenters.txt'), 'w') as f:
        for a in ans:
            f.write(a)
            f.write('\n')


def main():
    get_datacenters()
    zip_data()
    hosts = json.load(open(HOSTS_PATH))
    for host in hosts:
        hostname = host['hostname']
        username = host.get('username', 'johnsonli1993')
        password = host.get('password', 'johnsonli1993')
        region = host.get('region', 'unknown')
        conduct_experiment(hostname, username, password, region)


if __name__ == "__main__":
    main()
