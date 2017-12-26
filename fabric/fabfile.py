import os

from fabric.api import run, env, sudo

env.use_ssh_config = True
env.ssh_config_path = os.path.dirname(os.path.dirname(__file__)) + '/resources/ssh/config'


def host_type():
    run('uname -a')


def setup_bridge():
    sudo('whoami')
