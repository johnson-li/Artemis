from experiment.gcloud.main2 import *


if __name__ == '__main__':
    start = time.time()
    conduct_experiment(get_instances())
    end = time.time()
    print("time: ", end - start)

