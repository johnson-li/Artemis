import logging

import _mysql

db = _mysql.connect(host="35.228.52.213", user='johnson', passwd='welcOme0!')


def measure():
    logging.warning("start measuring...")


def main():
    logging.warning("start user mapping...")
    measure()


if __name__ == '__main__':
    main()
