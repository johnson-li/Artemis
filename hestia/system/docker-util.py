import docker
import docker.types

client = docker.from_env()

SID_CONTAINER_NAME = "johnson163/sid"
SID_CONTAINER_VERSION = 'version1.0'
SID_CONTAINER = '%s:%s' % (SID_CONTAINER_NAME, SID_CONTAINER_VERSION)
SID_NETWORK = 'sid-bridge'
SID_SUBNET_PREFIX = '172.18.1'
SID_SUBNET = '%s.0/24' % SID_SUBNET_PREFIX


def init_network():
    if not get_network():
        ipam_pool = docker.types.IPAMPool(subnet=SID_SUBNET, gateway='%s.1' % SID_SUBNET_PREFIX)
        ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])
        client.networks.create(SID_NETWORK, driver="bridge", ipam=ipam_config)


def get_network():
    networks = client.networks.list(names=[SID_NETWORK])
    return networks[0] if networks else None


def clear_containers():
    containers = client.containers.list(all=True)
    containers = list(filter(lambda c: c.attrs['Name'].startswith('/sid_'), containers))
    for container in containers:
        print("Remove container: %s(%s)" % (container.attrs['Name'], container.attrs['Id']))
        container.stop(timeout=1)
        container.remove()


def create_containers(num=1):
    client.images.pull(SID_CONTAINER)
    started = []
    network = get_network()
    for i in range(num):
        name = 'sid_%s' % i
        if not client.containers.list(filters={'name': name}):
            container = client.containers.create(SID_CONTAINER, name=name, network=SID_NETWORK, stdin_open=True)
            network.connect(container, ipv4_address="%s.%s" % (SID_SUBNET_PREFIX, i + 100))
            container.start()
            started.append(container)
            print("Container started: %s(%s)" % (container.attrs['Name'], container.attrs['Id']))


def get_container_info():
    containers = client.containers.list(all=True)
    containers = list(filter(lambda c: c.attrs['Name'].startswith('/sid_'), containers))
    print([c.attrs['Name'] for c in containers])


def test():
    init_network()
    clear_containers()
    create_containers(2)
    get_container_info()


if __name__ == '__main__':
    test()
