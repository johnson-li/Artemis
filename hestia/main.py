import sys

import botocore.exceptions

from hestia.aws.sessions import Sessions


def get_sessions():
    sessions = Sessions()
    return sessions


def stop(session):
    resource = session.resource('ec2')
    for instance in resource.instances.all():
        if instance.state['Name'] == 'running':
            instance.stop()


def start(session):
    resource = session.resource('ec2')
    for instance in resource.instances.all():
        if instance.state['Name'] == 'stopped':
            instance.start()


def clear_interfaces(session):
    resource = session.resource('ec2')
    for interface in resource.network_interfaces.all():
        try:
            interface.delete()
        except botocore.exceptions.ClientError as e:
            print(e.response['Error']['Message'], file=sys.stderr)
    for subnet in resource.subnets.all():
        try:
            subnet.delete()
        except botocore.exceptions.ClientError as e:
            print(e.response['Error']['Message'], file=sys.stderr)
    for security_group in resource.security_groups.all():
        try:
            security_group.delete()
        except botocore.exceptions.ClientError as e:
            print(e.response['Error']['Message'], file=sys.stderr)
    for vpc in resource.vpcs.all():
        try:
            vpc.delete()
        except botocore.exceptions.ClientError as e:
            print(e.response['Error']['Message'], file=sys.stderr)


def create_interfaces(session):
    resource = session.resource('ec2')
    vpc = resource.create_vpc(CidrBlock='10.0.0.0/24', AmazonProvidedIpv6CidrBlock=True)
    print('created vpc: ' + str(vpc))
    while not vpc.ipv6_cidr_block_association_set[0]['Ipv6CidrBlock']:
        vpc.reload()

    subnet = resource.create_subnet(AvailabilityZone=session.region_name + 'a', CidrBlock=vpc.cidr_block, VpcId=vpc.id,
                                    Ipv6CidrBlock=vpc.ipv6_cidr_block_association_set[0]['Ipv6CidrBlock'][:-2] + '64')
    print('created subnet: ' + str(subnet))
    security_group = resource.create_security_group(Description='All Pass', GroupName='all_pass', VpcId=vpc.id)
    security_group.authorize_ingress(
        IpPermissions=[
            {
                'FromPort': 0,
                'IpProtocol': '-1',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                    },
                ],
                'Ipv6Ranges': [
                    {
                        'CidrIpv6': '::/0',
                    },
                ],
                'ToPort': 65535,
                'UserIdGroupPairs': [
                    {
                        'GroupId': security_group.id,
                        'VpcId': vpc.id,
                    },
                ]
            },
        ],
    )
    print('created security group: ' + str(security_group))
    interfaces = []
    for i in range(1, 5):
        interface = resource.create_network_interface(
            Description='eth' + str(i),
            Groups=[
                security_group.id,
            ],
            Ipv6AddressCount=1,
            SubnetId=subnet.id
        )
        interfaces.append(interface)
    print('created interfaces: ' + str(interfaces))
    return vpc, subnet, security_group, interfaces


def clear_instances(session):
    ec2 = session.resource('ec2')
    for instance in ec2.instances.all():
        instance.terminate()


def create_instances(session, vpc):
    ec2 = session.resource('ec2')
    instance = ec2.create_instances(
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',
                'Ebs': {
                    'DeleteOnTermination': True,
                    'SnapshotId': 'snap-0dcc947e7c10bed94',
                    'VolumeSize': 8,
                    'VolumeType': 'gp2'
                },
                #         'NoDevice': 'string'
            },
        ],
        ImageId='ami-aa2ea6d0',
        InstanceType='t2.micro',
        Ipv6AddressCount=1,
        # Ipv6Addresses=[
        #     {
        #         'Ipv6Address': 'string'
        #     },
        # ],
        # KernelId='ami-aa2ea6d0',
        KeyName='virginia',
        MaxCount=1,
        MinCount=1,
        Monitoring={
            'Enabled': False
        },
        Placement={
            'AvailabilityZone': session.region_name + 'a',
            #     'Affinity': 'string',
            #     'GroupName': 'string',
            #     'HostId': 'string',
            #     'Tenancy': 'default' | 'dedicated' | 'host',
            #     'SpreadDomain': 'string'
        },
        # RamdiskId='string',
        # SecurityGroupIds=[
        #     security_group.id,
        # ],
        # SecurityGroups=[
        #     'string',
        # ],
        # SubnetId=subnet.id,
        # UserData='string',
        # AdditionalInfo='string',
        # ClientToken='string',
        # DisableApiTermination=True | False,
        # DryRun=True | False,
        # EbsOptimized=True | False,
        # IamInstanceProfile={
        #     'Arn': 'string',
        #     'Name': 'string'
        # },
        # InstanceInitiatedShutdownBehavior='stop' | 'terminate',
        NetworkInterfaces=[
            {
                'AssociatePublicIpAddress': True,
                'DeleteOnTermination': True,
                #         'Description': 'string',
                'DeviceIndex': 0,
                'Groups': [
                    security_group.id,
                ],
                'Ipv6AddressCount': 1,
                #         'Ipv6Addresses': [
                #             {
                #                 'Ipv6Address': 'string'
                #             },
                #         ],
                # 'NetworkInterfaceId': interfaces[0].id,
                #         'PrivateIpAddress': 'string',
                #         'PrivateIpAddresses': [
                #             {
                #                 'Primary': True | False,
                #                 'PrivateIpAddress': 'string'
                #             },
                #         ],
                #         'SecondaryPrivateIpAddressCount': 123,
                'SubnetId': subnet.id
            },
            # {
            #     'DeviceIndex': 1,
            #     'Groups': [
            #         security_group.id,
            # ],
            # 'NetworkInterfaceId': interfaces[1].id,
            # }
        ],
        # PrivateIpAddress='string',
        # ElasticGpuSpecification=[
        #     {
        #         'Type': 'string'
        #     },
        # ],
        # TagSpecifications=[
        #     {
        #         'ResourceType': 'customer-gateway' | 'dhcp-options' | 'image' | 'instance' | 'internet-gateway' | 'network-acl' | 'network-interface' | 'reserved-instances' | 'route-table' | 'snapshot' | 'spot-instances-request' | 'subnet' | 'security-group' | 'volume' | 'vpc' | 'vpn-connection' | 'vpn-gateway',
        #         'Tags': [
        #             {
        #                 'Key': 'string',
        #                 'Value': 'string'
        #             },
        #         ]
        #     },
        # ],
        # LaunchTemplate={
        #     'LaunchTemplateId': 'string',
        #     'LaunchTemplateName': 'string',
        #     'Version': 'string'
        # },
        # InstanceMarketOptions={
        #     'MarketType': 'spot',
        #     'SpotOptions': {
        #         'MaxPrice': 'string',
        #         'SpotInstanceType': 'one-time' | 'persistent',
        #         'BlockDurationMinutes': 123,
        #         'ValidUntil': datetime(2015, 1, 1),
        #         'InstanceInterruptionBehavior': 'hibernate' | 'stop' | 'terminate'
        #     }
        # },
        # CreditSpecification={
        #     'CpuCredits': 'string'
        # }
    )
    ec2.attach_network_interface(DeviceIndex=1, NetworkInterfaceId=interfaces[1].id, InstanceId=instance.id)
    print("created instance: " + str(instance))


def clear_all(session):
    clear_instances(session)
    clear_interfaces(session)


def enable_subnet_with_ipv6(session):
    vpc = session.resource('vpc')




def main():
    sessions = get_sessions()
    # parameters = create_interfaces(sessions.us_east_1)
    # create_instances(sessions.us_west_2)
    # clear_all(sessions.us_east_1)
    for zone in sessions.all():
        enable_subnet_with_ipv6(zone)


if __name__ == '__main__':
    main()
