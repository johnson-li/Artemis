import os

from fabric.api import run, env, sudo, parallel

env.warn_only = True
env.skip_bad_hosts = True
env.use_ssh_config = True
env.ssh_config_path = os.path.dirname(os.path.dirname(__file__)) + '/resources/ssh/config'

env.hosts = ['virginia-router', 'virginia-server', 'ohio-server', 'ohio-router', 'california-router', 'california-server', 'oregon-server', 'oregon-router', 'mumbai-server', 'mumbai-router', 'singapore-router', 'singapore-server', 'sydney-router', 'sydney-server', 'tokyo-router', 'tokyo-server', 'seoul-router', 'seoul-server', 'central-router', 'central-server', 'frankfurt-router', 'frankfurt-server', 'ireland-router', 'ireland-server', 'london-server', 'london-router',
        'paris-server', 'paris-router', 'saopaulo-server', 'saopaulo-router']


@parallel(pool_size=4)
def host_type():
    run('uname -a')


@parallel(pool_size=4)
def setup_bridge():
    sudo('/usr/local/share/openvswitch/scripts/ovs-ctl start')
    sudo('ovs-vsctl show')
