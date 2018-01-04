import pprint

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.main_database
collection = db.experiment_collection


def store(hostname, ip, direct_data, dns_data, sid_data, time):
    data = {
        'hostname': hostname,
        'ip': ip,
        'direct_data': direct_data,
        'dns_data': dns_data,
        'sid_data': sid_data,
        'time': time
    }
    record_id = collection.insert_one(data)
    print(record_id)


def query():
    print(collection.count())
    pprint.pprint(collection.find_one())


def main():
    store("localhost", '127.0.0.1', [1, 2, 3], [2, 3, 4], [2, 3, 4], '2017-01-01 11:12:23')
    query()


if __name__ == '__main__':
    main()
