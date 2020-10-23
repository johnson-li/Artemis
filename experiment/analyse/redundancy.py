from experiment.analyse.zones import handle_region
import os
from hestia import PROJECT_PATH

DATA_PATH = os.path.join(PROJECT_PATH, f'resources/exp3')


def main():
    files = (('res1/mysql.dump', 'dup 1'), ('res2/mysql.dump', 'dup 2'),
             ('res3/mysql.dump', 'dup 3'), ('res4/mysql.dump', 'dup 4'))
    for file_name, name in files:
        os.system(f'mysql -pjohnson serviceid_db < {os.path.join(DATA_PATH, file_name)}')
        handle_region(name, name == 'dup 4')


if __name__ == '__main__':
    main()
