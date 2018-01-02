import os

from fabric.api import *
from fabric.io import CommandTimeout

env.warn_only = True
env.skip_bad_hosts = True
env.use_ssh_config = True
env.ssh_config_path = os.path.dirname(os.path.dirname(__file__)) + '/resources/ssh/config'

env.hosts = ['virginia-router', 'virginia-server', 'ohio-server', 'ohio-router', 'california-router',
             'california-server', 'oregon-server', 'oregon-router', 'mumbai-server', 'mumbai-router',
             'singapore-router', 'singapore-server', 'sydney-router', 'sydney-server', 'tokyo-router', 'tokyo-server',
             'seoul-router', 'seoul-server', 'central-router', 'central-server', 'frankfurt-router', 'frankfurt-server',
             'ireland-router', 'ireland-server', 'london-server', 'london-router',
             'paris-server', 'paris-router', 'saopaulo-server', 'saopaulo-router']
env.hosts = ['tokyo-router', 'tokyo-server']


@parallel(pool_size=4)
def host_type():
    run('uname -a')


@parallel(pool_size=4)
def setup_bridge():
    result = run('ifconfig eth1| grep "inet addr"')
    add_eth1 = result.return_code != 0
    if add_eth1:
        sudo('bash -c "echo \'auto eth1\niface eth1 inet dhcp\niface eth1 inet6 dhcp\' >>'
             ' /etc/network/interfaces.d/50-cloud-init.cfg"')
        try:
            sudo('/etc/init.d/networking restart', timeout=5)
        except CommandTimeout as e:
            print(e)
    # sudo('/usr/local/share/openvswitch/scripts/ovs-ctl start')
    sudo('sysctl -w net.ipv4.ip_forward=1')
    # sudo('ovs-vsctl del-br br1')
    # sudo('ovs-vsctl add-br br1')
    ipv4_0 = run("ifconfig eth0|grep 'inet addr'| gawk 'match($0, /inet addr:(.*?)  Bcast/, ary) {print ary[1]}'")
    ipv4_1 = run("ifconfig eth1|grep 'inet addr'| gawk 'match($0, /inet addr:(.*?)  Bcast/, ary) {print ary[1]}'")
    ipv6 = run("ifconfig eth1|grep 'Global'| gawk 'match($0, /inet6 addr: (.*?) Scope/, ary) {print ary[1]}'")
    mac_eth = run("ifconfig eth1|grep 'HWaddr'| gawk 'match($0, /HWaddr (.*?)  /, ary) {print ary[1]}'")
    mac_br = run("ifconfig br1|grep 'HWaddr'| gawk 'match($0, /HWaddr (.*?)  /, ary) {print ary[1]}'")
    gateway = run("route -n| gawk 'match($0, /0\.0\.0\.0 +([0-9.]+).*eth0/, ary) {print ary[1]}'| head -n1")
    # sudo('ifconfig br1 {}/20 up'.format(ipv4_1))
    # sudo('ifconfig br1 inet6 add {}'.format(ipv6))
    # sudo('ovs-vsctl add-port br1 eth1')
    # sudo('ovs-ofctl add-flow br1 priority=100,in_port=eth1,actions=mod_dl_dst:{},local'.format(mac_br))
    # sudo('ovs-ofctl add-flow br1 priority=100,in_port=local,actions=mod_dl_src:{},eth1'.format(mac_eth))
    # sudo('ifconfig eth1 0')
    sudo('ip route add default via {} dev eth0 tab 1'.format(gateway))
    sudo('ip route add default via {} dev eth1 tab 2'.format(gateway))
    sudo('ip rule add from {}/24 tab 1 priority 500'.format(ipv4_0))
    sudo('ip rule add from {}/24 tab 2 priority 600'.format(ipv4_1))
