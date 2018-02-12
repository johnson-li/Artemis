import re


def main():
    data = {}
    for line in open('/Users/johnson/output'):
        if 'OFPT_FEATURES_REPLY' in line:
            groups = re.match('\[([a-z]+)-([a-z]+)\].*dpid:([0-9a-z]+)', line.strip()).groups()
            data.setdefault(groups[0].lower(), {})
            data[groups[0].lower()][groups[1]] = ':'.join(
                [groups[2][i * 2: i * 2 + 2] for i in range(int(len(groups[2]) / 2))])
    print(data)


if __name__ == '__main__':
    main()
