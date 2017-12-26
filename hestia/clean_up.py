from hestia.aws.sessions import Sessions


def main():
    sessions = Sessions()
    for session in sessions.all():
        ec2 = session.resource('ec2')
        for instance in ec2.instances.all():
            print('Stop instance: {} in region: {}'.format(str(instance), session.region_name))
            instance.stop()


if __name__ == '__main__':
    main()
