import os.path

from numpy import percentile

from hestia import RESOURCE_PATH, MATLAB_PATH

SID_PATH = RESOURCE_PATH + '/data/sid'
OUTPUT_PATH = MATLAB_PATH + '/benchmark.m'


def latency():
    end = 101
    handshake_latencies = [[] for _ in range(end)]
    transfer_latencies = [[] for _ in range(end)]
    client_mems = [0 for _ in range(end)]
    client_cpus = [0 for _ in range(end)]
    server_mems = [0 for _ in range(end)]
    server_cpus = [0 for _ in range(end)]
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
        if os.path.isfile(SID_PATH + '/dir-c%d.mem' % i):
            with open(SID_PATH + '/dir-c%d.mem' % i) as f:
                mem = int(f.read())
                client_mems[i] = mem / 1024
        with open(SID_PATH + '/dir-s%d.mem' % i) as f:
            mem = int(f.read())
            server_mems[i] = mem / 1024
        if os.path.isfile(SID_PATH + '/dir-c%d.cpu' % i):
            with open(SID_PATH + '/dir-c%d.cpu' % i) as f:
                max_cpu = 0
                for line in f.readlines():
                    line = line.strip()
                    if line:
                        try:
                            cpu = float(line)
                            if cpu > max_cpu:
                                max_cpu = cpu
                        except Exception:
                            pass
                client_cpus[i] = max_cpu
        if os.path.isfile(SID_PATH + '/dir-s%d.cpu' % i):
            with open(SID_PATH + '/dir-s%d.cpu' % i) as f:
                max_cpu = 0
                for line in f.readlines():
                    line = line.strip()
                    if line and not line.startswith('C') and not line.startswith('/'):
                        try:
                            cpu = float(line)
                            if cpu > max_cpu:
                                max_cpu = cpu
                        except Exception:
                            pass
                server_cpus[i] = max_cpu
    print('hs = %s / 1000;' % str([percentile(handshake_latencies[i], 50) for i in range(1, end)]))
    print('tf = %s / 1000;' % str([percentile(transfer_latencies[i], 50) for i in range(1, end)]))
    print('client mems = %s' % client_mems[1:])
    print('client cpus = %s' % client_cpus[1:])
    print('server mems = %s' % client_mems[1:])
    print('server cpus = %s' % client_cpus[1:])
    print('bar([hs; tf]\');')
    with open(OUTPUT_PATH, 'w') as f:
        lines = [
            # =====latencies=====
            'hs = %s / 1000;' % str([percentile(handshake_latencies[i], 50) for i in range(1, end)]),
            'tf = %s / 1000;' % str([percentile(transfer_latencies[i], 50) for i in range(1, end)]),
            "bar([hs; tf]');",
            "xlabel('Number of connections');",
            "ylabel('Latency (ms)')",
            "set(gca,'FontSize',20)",
            "pbaspect([2 1 1])",
            "axis([1 100 0 600])",
            "legend('handshake latency', 'transport latency');",
            "print('figures/direct-latency','-depsc');",
            # =====cpu=====
            "cpu_cli = %s;" % client_cpus[1:],
            "cpu_ser = %s;" % server_cpus[1:],
            "bar([cpu_cli; cpu_ser]');",
            "xlabel('Number of connections');",
            "ylabel('CPU usage (%)')",
            "set(gca,'FontSize',20)",
            "pbaspect([2 1 1])",
            "axis([1 100 0 13])",
            "legend('client', 'server');",
            "print('figures/direct-cpu','-depsc');",
            # =====memory=====
            "mem_cli = %s;" % client_mems[1:],
            "mem_ser = %s;" % server_mems[1:],
            "bar([mem_cli; mem_ser]');",
            "xlabel('Number of connections');",
            "ylabel('Memory (MB)')",
            "pbaspect([2 1 1])",
            "axis([1 100 25 42])",
            "set(gca,'FontSize',20)",
            "legend('client', 'server');",
            "print('figures/direct-memory','-depsc');",
        ]
        f.writelines([l + '\n' for l in lines])


def main():
    latency()


if __name__ == '__main__':
    main()
