def main():
    data = {
        'us-central1-c-server': 'a6:99:21:1f:28:4c',
        'us-east4-c-server': '46:4e:66:cf:84:48',
        'us-west1-c-server': '72:d4:a5:16:29:46',
        'us-east1-c-server': 'ca:9f:e8:4c:9d:42',
        'europe-west4-c-server': 'ae:30:ce:67:71:43',
        'europe-west3-c-server': '7a:bf:87:52:26:4d',
        'europe-west2-c-server': '2e:f1:8f:a3:89:49',
        'europe-west1-c-server': 'd6:4e:1c:ca:8f:4f',
    }
    res = {}
    for key, val in data.items():
        k1 = key[-6:]
        k2 = key[: -7]
        res[k2] = {'server': {'br1': val}}
    print(res)


if __name__ == '__main__':
    main()
