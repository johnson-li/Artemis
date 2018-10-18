import docker

client = docker.from_env()


def clear_containers():
    print(client.containers.list())


def create_containers():
    pass


def get_container_info():
    pass


def test():
    clear_containers()


if __name__ == '__main__':
    test()
