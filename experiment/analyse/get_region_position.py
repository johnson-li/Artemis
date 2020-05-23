import csv


def region2position(region_name):
    with open("position-list.csv") as csv_reader:
        f_csv = csv.reader(csv_reader)
        flag = 0
        for line in f_csv:
            if not flag:
                flag = 1
                continue
            if line[0] == region_name:
                return [line[2], line[1]]
            # print(line)

