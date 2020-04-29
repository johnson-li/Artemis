from experiment.gcloud.main import *


if __name__ == '__main__':
    start = time.time()
    conduct_experiment(get_instances())
    end = time.time()
    print("time: ", end - start)

