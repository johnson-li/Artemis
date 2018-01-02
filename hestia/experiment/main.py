import paramiko

from hestia import RESOURCE_PATH


def get_latency(host, peer):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_config = paramiko.SSHConfig()
    with open(RESOURCE_PATH + '/ssh/config') as f:
        ssh_config.parse(f)
    cfg = ssh_config.lookup(host)
    ssh.connect(cfg['hostname'], username=cfg['user'], key_filename=cfg['identityfile'])
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
        "ping -c 10 " + peer + " | tail -1| awk '{print $4}' | cut -d '/' -f 2")
    for line in ssh_stdout:
        return float(line)


if __name__ == '__main__':
    hosts = ['tokyo-router', 'tokyo-server']
    results = []
    for host in hosts:
        results.append((host, get_latency("tokyo-server", "google.com")))
    results.sort(key=lambda pair: pair[1])
    print(results)
