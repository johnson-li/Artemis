from multiprocessing import Pool
from time import sleep, time


def f(x):
    sleep(1)
    return x[0], x[0] * x[1]


if __name__ == '__main__':
    p = Pool(2)
    print(time())
    print(p.starmap(f, [1, 2]))
    print(time())
