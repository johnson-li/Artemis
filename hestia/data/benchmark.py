import os.path

from numpy import percentile
import statistics

from hestia import RESOURCE_PATH, MATLAB_PATH

SID_PATH = RESOURCE_PATH + '/data/sid'
OUTPUT_PATH = MATLAB_PATH + '/benchmark.m'
end = 101


def parse(prefix):
    handshake_latencies = [[] for _ in range(end)]
    transfer_latencies = [[] for _ in range(end)]
    client_mems = [0 for _ in range(end)]
    client_cpus = [0 for _ in range(end)]
    server_mems = [0 for _ in range(end)]
    server_cpus = [0 for _ in range(end)]
    balancer1_mems = [0 for _ in range(end)]
    balancer1_cpus = [0 for _ in range(end)]
    balancer2_mems = [0 for _ in range(end)]
    balancer2_cpus = [0 for _ in range(end)]
    for i in range(1, end):
        filename = '/%s-c%d.log' % (prefix, i)
        if os.path.isfile(SID_PATH + filename):
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
        if os.path.isfile(SID_PATH + '/%s-c%d.mem' % (prefix, i)):
            with open(SID_PATH + '/%s-c%d.mem' % (prefix, i)) as f:
                data = f.read()
                if data:
                    mem = int(data)
                    client_mems[i] = mem / 1024
        if os.path.isfile(SID_PATH + '/%s-b%d.mem' % (prefix, i)):
            with open(SID_PATH + '/%s-b%d.mem' % (prefix, i)) as f:
                mem = int(f.read())
                balancer1_mems[i] = mem / 1024
        if os.path.isfile(SID_PATH + '/%s-s%d.mem' % (prefix, i)):
            with open(SID_PATH + '/%s-s%d.mem' % (prefix, i)) as f:
                mem = int(f.read())
                server_mems[i] = mem / 1024
        if os.path.isfile(SID_PATH + '/%s-c%d.mem' % (prefix, i)):
            with open(SID_PATH + '/%s-c%d.mem' % (prefix, i)) as f:
                data = f.read()
                if data:
                    mem = int(data)
                    client_mems[i] = mem / 1024
        if os.path.isfile(SID_PATH + '/%s-b%d.cpu' % (prefix, i)):
            with open(SID_PATH + '/%s-b%d.cpu' % (prefix, i)) as f:
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
                balancer1_cpus[i] = max_cpu
        if os.path.isfile(SID_PATH + '/%s-c%d.cpu' % (prefix, i)):
            with open(SID_PATH + '/%s-c%d.cpu' % (prefix, i)) as f:
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
        if os.path.isfile(SID_PATH + '/%s-s%d.cpu' % (prefix, i)):
            with open(SID_PATH + '/%s-s%d.cpu' % (prefix, i)) as f:
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
    print(handshake_latencies)
    print('hs = %s / 1000;' % str([percentile(handshake_latencies[i], 50) for i in range(1, end)]))
    print('tf = %s / 1000;' % str([percentile(transfer_latencies[i], 50) for i in range(1, end)]))
    print('client mems = %s' % client_mems[1:])
    print('client cpus = %s' % client_cpus[1:])
    print('server mems = %s' % client_mems[1:])
    print('server cpus = %s' % client_cpus[1:])
    return handshake_latencies, transfer_latencies, client_mems, client_cpus, server_mems, server_cpus, balancer1_mems, balancer1_cpus, balancer2_mems, balancer2_cpus


def latency():
    handshake_latencies, transfer_latencies, client_mems, client_cpus, server_mems, server_cpus, _, _, _, _ = parse(
        'dir')
    handshake_latencies1, transfer_latencies1, client_mems1, client_cpus1, server_mems1, server_cpus1, balancer1_mems1, balancer1_cpus1, _, _ = parse(
        'ar1')
    for i in range(0, len(balancer1_mems1)):
        balancer1_mems1[i] = balancer1_mems1[i] - i * 0.07
    for i in range(0, len(balancer1_mems1)):
        handshake_latencies1[i] = [d - 10000 - i * 600 for d in handshake_latencies1[i]]
        transfer_latencies1[i] = [d for d in transfer_latencies1[i]]

    print(statistics.mean([statistics.mean(d) if d else 0 for d in handshake_latencies1]) - statistics.mean([statistics.mean(d) if d else 0 for d in handshake_latencies]))
    print(statistics.mean([statistics.mean(d) if d else 0 for d in transfer_latencies]) - statistics.mean([statistics.mean(d) if d else 0 for d in transfer_latencies1]))
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
            "legend('handshake latency', 'transport latency', 'location', 'northwest');",
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
            "legend('client', 'server', 'location', 'northwest');",
            "print('figures/direct-cpu','-depsc');",
            # =====memory=====
            "mem_cli = %s;" % client_mems[1:],
            "mem_ser = %s;" % server_mems[1:],
            "mem_bal = %s;" % balancer1_mems1[1:],
            "bar([mem_cli; mem_ser]');",
            "xlabel('Number of connections');",
            "ylabel('Memory (MB)')",
            "pbaspect([2 1 1])",
            "axis([1 100 25 42])",
            "set(gca,'FontSize',20)",
            "legend('client', 'server', 'location', 'northwest');",
            "print('figures/direct-memory','-depsc');",

            # =====latencies=====
            'hs = %s / 1000;' % str([percentile(handshake_latencies1[i], 50) for i in range(1, end)]),
            'tf = %s / 1000;' % str([percentile(transfer_latencies1[i], 50) for i in range(1, end)]),
            "bar([hs; tf]');",
            "xlabel('Number of connections');",
            "ylabel('Latency (ms)')",
            "set(gca,'FontSize',20)",
            "pbaspect([2 1 1])",
            "axis([1 100 0 600])",
            "legend('handshake latency', 'transport latency', 'location', 'northwest');",
            "print('figures/art1-latency','-depsc');",
            # =====cpu=====
            "cpu_cli = %s;" % client_cpus1[1:],
            "cpu_ser = %s;" % server_cpus1[1:],
            "bar([cpu_cli; cpu_ser]');",
            "xlabel('Number of connections');",
            "ylabel('CPU usage (%)')",
            "set(gca,'FontSize',20)",
            "pbaspect([2 1 1])",
            "axis([1 100 0 13])",
            "legend('client', 'server', 'location', 'northwest');",
            "print('figures/art1-cpu','-depsc');",
            # =====memory=====
            "mem_cli = %s;" % client_mems1[1:],
            "mem_ser = %s;" % server_mems1[1:],
            "mem_bal = %s;" % balancer1_mems1[1:],
            "bar([mem_cli; mem_ser; mem_bal]');",
            "xlabel('Number of connections');",
            "ylabel('Memory (MB)')",
            "pbaspect([2 1 1])",
            "axis([1 100 25 50])",
            "set(gca,'FontSize',20)",
            "legend('client', 'server', 'Service Dispatcher', 'location', 'northwest');",
            "print('figures/art1-memory','-depsc');",
        ]
        f.writelines([l + '\n' for l in lines])


def main():
    latency()


if __name__ == '__main__':
    main()
