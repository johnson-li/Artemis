from MySQLdb import _mysql
import matplotlib.pyplot as plt

from pprint import pprint


def main():
    db = _mysql.connect("34.68.107.26", "johnson", "johnson", "serviceid_db")
    db.query("select * from transfer_time")
    r = db.store_result()
    ans = {}
    while True:
        a = r.fetch_row()
        if not a:
            break
        a = a[0]
        k = a[4].decode("utf-8")[7:].replace('-', '')
        ans.setdefault(k, [])
        ans[k].append((a[6].decode("utf-8")[7:-7].replace('-', ''), a[7].decode("utf-8")[6:], float(a[8]), float(a[9]), float(a[10])))
    diffs = []
    keys = []
    dns = []
    diffs2 = []
    for key, val in ans.items():
        print(key)
        print([(v[0] == v[1]) for v in val])
        # print(val)
        keys.append(key)
        diff = [i[2] - i[4] for i in val]
        diffs.append(sum(diff) / len(diff) / 1000)
        diffs2.append(sum(diff) / len(diff) / 1000 - max([i[3] for i in val]))
        dns.append(max([i[3] for i in val]))
    fig = plt.figure()
    plt.barh(keys, diffs2)
    plt.xlabel('vLatency(Artemis) - Latency(DNS with query) in ms')
    plt.ylabel('Client region')
    plt.show()


if __name__ == '__main__':
    main()
