from hestia.aws.sessions import Sessions


def main():
    sessions = Sessions().all()
    for session in sessions:
        pass


if __name__ == '__main__':
    main()
