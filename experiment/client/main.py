import json
import os
import paramiko
import zipfile
from experiment.gcloud.logging import logging
from shutil import copyfile


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(DIR_PATH))
HOSTS_PATH = os.path.join(DIR_PATH, "data/hosts.json")
REMOTE_PROJECT_PATH = '/tmp/hestia'
DATA_PATH = os.path.join(DIR_PATH, 'data')
DATA_ZIP_PATH = os.path.join(DIR_PATH, 'data.zip')
logger = logging.getLogger(__name__)


def zip_data():
    copyfile('%s/machine.json' % PROJECT_PATH, '%s/data/machine.json' % DIR_PATH)
    copyfile('%s/ngtcp2/examples/client' % os.path.dirname(PROJECT_PATH),
             '%s/data/client' % DIR_PATH)
    zipf = zipfile.ZipFile(DATA_ZIP_PATH, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(DATA_PATH):
        for file in files:
            zipf.write(os.path.join(root, file),
                       arcname=os.path.join(root[len(DIR_PATH) + 1:], file))
    zipf.close()


def execute_ssh_sync(client, command):
    stdin, stdout, stderr = client.exec_command(command)
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
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password,
                   pkey=paramiko.RSAKey.from_private_key_file("/home/johnsonli1993/.ssh/id_rsa"))
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
    experiment_script = '%s/data/start.sh' % REMOTE_PROJECT_PATH
    execute_ssh_sync(client,
                     'export region=%s; chmod +x %s && %s' % (region, experiment_script, experiment_script))


def get_datacenters():
    data = json.load(open(os.path.join(DIR_PATH, "../../machine.json")))
    ans = ['%s %s' % (i[7:-7], data[i]['external_ip1'])
           for i in data.keys() if i.endswith('router')]
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
        region = host.get('region', '')
        conduct_experiment(hostname, username, password, region)


if __name__ == "__main__":
    main()
