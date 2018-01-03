from hestia.aws.sessions import Sessions


def release_ips(sessions):
    print('Release IPs')
    for session in sessions:
        ec2 = session.client('ec2')
        response = ec2.describe_addresses()
        addresses = response['Addresses']
        for address in addresses:
            ec2.release_address(AllocationId=address['AllocationId'])


def main():
    sessions = Sessions()
    session_list = [sessions.ap_northeast_1, sessions.ap_southeast_2, sessions.ap_southeast_1]
    pending_instances = []
    for session in session_list:
        ec2 = session.resource('ec2')
        for instance in ec2.instances.all():
            print('Stop instance: {} in region: {}'.format(str(instance), session.region_name))
            instance.stop()
            pending_instances.append(instance)
    release_ips(session_list)
    print('Wait for instances')
    while pending_instances:
        instance = pending_instances.pop(0)
        instance.load()
        if instance.state["Name"] != 'stopped':
            pending_instances.append(instance)


if __name__ == '__main__':
    main()
