#!/usr/bin/env python
import hestia.system.server


def init_system():
    """
        Install initial software and configure them. Get the application code.
    """
    pass


def start_applications():
    """
        Run application code
    """
    pass


def main():
    print("Starting ServiceID system...")
    hestia.system.server.start_servers()
    hestia.system.server.init_servers()
    init_system()
    start_applications()


if __name__ == '__main__':
    main()
