import logging
import os
import sys
import threading
import time
from multiprocessing.dummy import Pool as ThreadPool

import MySQLdb

pool = ThreadPool(4)

db = MySQLdb.connect(host="35.228.52.213", user='johnson', passwd='welcOme0!', db='sid')
db.autocommit(on=True)
dc = 'test'


def millis():
    return int(time.time())


def ping(client):
    res = os.popen("ping -c 5 %s | tail -1| awk '{print $4}' | cut -d '/' -f 2" % client).read()
    res = int(float(res))
    cursor = db.cursor()
    cursor.execute(
        "insert into measurements (dc, client, latency, ts) values ('%s', '%s', %d, %d)" % (dc, client, res, millis()))
    cursor.close()
    return res


def measure():
    cursor = db.cursor()
    cursor.execute('select ip from clients')
    rows = cursor.fetchall()
    clients = [[row[0]] for row in rows]
    logging.warning("client number: %d" % len(clients))
    pool.starmap(ping, clients)
    threading.Timer(60, measure).start()


def main():
    if len(sys.argv) > 1:
        global dc
        dc = sys.argv[1]
        logging.warning("dc: %s" % dc)
    measure()


if __name__ == '__main__':
    main()
