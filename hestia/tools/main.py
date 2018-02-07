import argparse


def main():
    parser = argparse.ArgumentParser(description='Setup gre bridges between hosts.')
    parser.add_argument('--peer', help='The IP of the client', default='123')
    args = parser.parse_args()
    print(args.peer)


if __name__ == '__main__':
    main()
