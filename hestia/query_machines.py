from hestia.aws.sessions import Sessions


def main():
    sessions = Sessions()
    for session in sessions.all():
        pass


if __name__ == '__main__':
    main()
