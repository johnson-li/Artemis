import os

from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from msrestazure.azure_exceptions import CloudError

DEFAULT_GROUP_NAME = "Hestia"
ZONES = ['westus', 'eastus', 'northeurope', 'westeurope', 'eastasia', 'southeastasia', 'northcentralus',
         'southcentralus', 'centralus', 'eastus2', 'japaneast', 'japanwest', 'brazilsouth', 'australiaeast',
         'australiasoutheast', 'centralindia', 'southindia', 'westindia', 'canadacentral', 'canadaeast',
         'westcentralus', 'westus2', 'ukwest', 'uksouth', 'koreacentral', 'koreasouth', 'francecentral',
         'australiacentral', 'southafricanorth', 'uaenorth', 'switzerlandnorth', 'germanywestcentral', 'norwayeast']
zones = ZONES[:2]

compute_client = get_client_from_auth_file(ComputeManagementClient,
                                           auth_path=os.path.expanduser("~/keys/azure-credentials.json"))
resource_client = get_client_from_auth_file(ResourceManagementClient,
                                            auth_path=os.path.expanduser("~/keys/azure-credentials.json"))
network_client = get_client_from_auth_file(NetworkManagementClient,
                                           auth_path=os.path.expanduser("~/keys/azure-credentials.json"))


def create_resource_group(group_name=DEFAULT_GROUP_NAME):
    try:
        res = resource_client.resource_groups.get(group_name)
        return res
    except CloudError as e:
        pass
    res = resource_client.resource_groups.create_or_update(
        group_name,
        {
            'location': 'northeurope'
        }
    )
    return res.result()


def create_public_ip(zone, address_name, group_name=DEFAULT_GROUP_NAME):
    try:
        res = network_client.public_ip_addresses.get(group_name, address_name)
        return res
    except CloudError as e:
        pass
    res = network_client.public_ip_addresses.create_or_update(
        group_name,
        address_name,
        {
            'location': zone,
            'public_ip_allocation_method': 'Dynamic'
        }
    )
    return res.result()


def create_network(network_name, zone, prefix='10.1.0.0/16', group_name=DEFAULT_GROUP_NAME):
    try:
        res = network_client.virtual_networks.get(group_name, network_name)
        return res
    except CloudError as e:
        pass
    ans = network_client.virtual_networks.create_or_update(
        group_name,
        network_name,
        {
            'location': zone,
            'address_space': {
                'address_prefixes': [prefix]
            }
        }
    )
    return ans.result()


def create_subnet(subnet_name, network_name, prefix='10.1.0.0/24', group_name=DEFAULT_GROUP_NAME):
    try:
        res = network_client.subnets.get(group_name, network_name, subnet_name)
        return res
    except CloudError as e:
        pass
    ans = network_client.subnets.create_or_update(
        group_name,
        network_name,
        subnet_name,
        {
            'address_prefix': prefix
        }
    )
    return ans.result()


def create_nic(nic_name, zone, subnet, ip_address, group_name=DEFAULT_GROUP_NAME):
    try:
        res = network_client.network_interfaces.get(group_name, nic_name)
        return res
    except CloudError as e:
        pass
    ans = network_client.network_interfaces.create_or_update(
        group_name,
        nic_name,
        {
            'location': zone,
            'ip_configurations': [{
                'name': '%s_config' % nic_name,
                'public_ip_address': ip_address,
                'subnet': {
                    'id': subnet.id
                }
            }]
        }
    )
    return ans.result()


def create_virtual_machine(name, zone, nic, group_name=DEFAULT_GROUP_NAME):
    try:
        ans = compute_client.virtual_machines.get(group_name, name)
        return ans
    except CloudError as e:
        pass
    ans = compute_client.virtual_machines.create_or_update(
        group_name,
        name,
        {
            'location': zone,
            'os_profile': {
                'computer_name': name,
                'admin_username': 'johnson',
                'admin_password': 'johnson',
            },
            'hardware_profile': {
                'vm_size': 'Standard_B1s'
            },
            'storage_profile': {
                'image_reference': {
                    'publisher': 'Canonical',
                    'offer': 'UbuntuServer',
                    'sku': '18.04-LTS',
                    'version': 'latest'
                }
            },
            'network_profile': {
                'network_interfaces': [{
                    'id': nic.id
                }]
            },
        }
    )
    return ans.result()


def delete_ip_addresses(group_name=DEFAULT_GROUP_NAME):
    for ip_address in network_client.public_ip_addresses.list(group_name):
        network_client.public_ip_addresses.delete(group_name, ip_address['name'])


def delete_resources(group_name=DEFAULT_GROUP_NAME):
    delete_ip_addresses(group_name)


def stop_virtual_machines():
    pass


def test():
    zone = 'northeurope'
    resource_group = create_resource_group()
    public_ip = create_public_ip(zone, 'a')
    network = create_network("net", zone)
    subnet = create_subnet("subnet", "net")
    nic = create_nic("nicnic", zone, subnet, public_ip)
    vm = create_virtual_machine("instance", zone, nic)
    print(vm)
    # delete_resources()
    pass


if __name__ == '__main__':
    test()
