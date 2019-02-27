from numpy import percentile

from hestia import RESOURCE_PATH

SID_PATH = RESOURCE_PATH + '/data/sid'


def latency():
    end = 11
    handshake_latencies = [[] for _ in range(end)]
    transfer_latencies = [[] for _ in range(end)]
    client_mems = [0 for _ in range(end)]
    client_cpus = [0 for _ in range(end)]
    server_mems = [0 for _ in range(end)]
    server_cpus = [0 for _ in range(end)]
    print('hold on;')
    for i in range(1, end):
        filename = '/dir-c%d.log' % i
        with open(SID_PATH + filename) as f:
            for line in f.readlines():
                if line.strip():
                    if line.startswith('handshake'):
                        l = int(line[16:])
                        handshake_latencies[i].append(l)
                    elif line.startswith('transfer'):
                        l = int(line[15:])
                        transfer_latencies[i].append(l)
                    else:
                        print("Unexpected line: " + line)
        with open(SID_PATH + '/dir-c%d.mem' % i) as f:
            mem = int(f.read())
            client_mems[i] = mem
        with open(SID_PATH + '/dir-s%d.mem' % i) as f:
            mem = int(f.read())
            server_mems[i] = mem
        with open(SID_PATH + '/dir-c%d.cpu' % i) as f:
            for line in f.readlines():
                max_cpu = 0
                if line.strip():
                    cpu = float(line.strip())
                    if cpu > max_cpu:
                        max_cpu = cpu
            client_cpus[i] = max_cpu
        with open(SID_PATH + '/dir-s%d.cpu' % i) as f:
            for line in f.readlines():
                max_cpu = 0
                if line.strip():
                    cpu = float(line.strip())
                    if cpu > max_cpu:
                        max_cpu = cpu
            server_cpus[i] = max_cpu
    print('hs = %s / 1000;' % str([percentile(handshake_latencies[i], 50) for i in range(1, end)]))
    print('tf = %s / 1000;' % str([percentile(transfer_latencies[i], 50) for i in range(1, end)]))
    print('client mems = %s' % client_mems[1:])
    print('client cpus = %s' % client_cpus[1:])
    print('server mems = %s' % client_mems[1:])
    print('server cpus = %s' % client_cpus[1:])
    print('bar([hs; tf]\');')


def main():
    latency()


if __name__ == '__main__':
    main()
