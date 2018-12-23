#!/usr/bin/env python
import logging

import yaml

import hestia.system.server
from hestia import RESOURCE_PATH

logging = logging


def init_logger():
    logging.getLogger("paramiko").setLevel(logging.WARNING)
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG)


def main():
    init_logger()
    logging.info("Starting ServiceID system...")
    with open(RESOURCE_PATH + "/system/platform.yaml", 'r') as stream:
        info = yaml.load(stream)
    logging.info("Platform: %s" % info['type'])
    if info['type'] == 'vmware-osx':
        server = hestia.system.server
    logging.info('start servers')
    server.start_servers()
    logging.info('init servers')
    server.init_servers()
    logging.info('init systems')
    server.init_systems()
    logging.info('start applications')
    server.start_applications()


if __name__ == '__main__':
    main()
