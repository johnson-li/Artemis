def main():
    data = {
        'us-central1-c-router': '000072a97e23cc43',
        'us-central1-c-server': '0000a699211f284c',
        'us-east4-c-router': '00003aa7191e2a47',
        'us-east4-c-server': '0000464e66cf8448',
        'us-west1-c-server': '000072d4a5162946',
        'us-west1-c-router': '0000f248ac425943',
        'us-east1-c-router': '0000c659f7869e48',
        'us-east1-c-server': '0000ca9fe84c9d42',
        'europe-west4-c-server': '0000ae30ce677143',
        'europe-west4-c-router': '000046a66c222f4e',
        'europe-west3-c-server': '00007abf8752264d',
        'europe-west3-c-router': '00002e9a4ae4174c',
        'europe-west2-c-server': '00002ef18fa38949',
        'europe-west2-c-router': '0000964cf934e943',
        'europe-west1-c-server': '0000d64e1cca8f4f',
        'europe-west1-c-router': '0000aade75682749',
    }
    res = {}
    for key, val in data.items():
        k1 = key[-6:]
        k2 = key[: -7]
        if k2 not in res:
            res[k2] = {}
        dd = ''
        count = 0
        for c in val:
            dd = dd + c
            count += 1
            if count == 2:
                dd = dd + ':'
                count = 0
        res[k2][k1] = dd[:-1]
    print(res)


if __name__ == '__main__':
    main()
