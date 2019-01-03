import threading
import time
from multiprocessing.dummy import Pool as ThreadPool

import MySQLdb

pool = ThreadPool(4)

db = MySQLdb.connect(host="35.228.52.213", user='johnson', passwd='welcOme0!', db='sid')


def millis():
    return int(time.time() * 1000)


def ping(client):
    # res = os.system("ping -c 5 %s | tail -1| awk '{print $4}' | cut -d '/' -f 2" % client)
    res = '4.32'
    res = float(res)
    cursor = db.cursor()
    cursor.execute(
        "insert into measurements (dc, client, latency, ts) values ('%s', '%s', %d, %d)" % ('', client, res, millis()))
    return res


def measure():
    cursor = db.cursor()
    cursor.execute('select ip from clients')
    rows = cursor.fetchall()
    clients = [[row[0]] for row in rows]
    pool.starmap(ping, clients)
    threading.Timer(10, measure).start()


def main():
    measure()


if __name__ == '__main__':
    main()
