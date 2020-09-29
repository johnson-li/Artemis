from experiment.aws.utils import start
import argparse


def main():
    parser = argparse.ArgumentParser(description='Start AWS machines as hosts')
    parser.add_argument('--range', help='The start index and the end index of hosts')
    args = parser.parse_args()
    ra = [int(r) for r in args.range.split(',')]
    start(ra[0], ra[1])


if __name__ == '__main__':
    main()
