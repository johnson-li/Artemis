from hestia import RESOURCE_PATH
from numpy import percentile

SID_PATH = RESOURCE_PATH + '/data/sid'


def latency():
    end = 11
    handshake_latencies = [[] for _ in range(end)]
    transfer_latencies = [[] for _ in range(end)]
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
            # print('hs' + str(i) + " = " + str(handshake_latencies[i]) + ";")
            # print('tf' + str(i) + " = " + str(transfer_latencies[i]) + ";")
    # print("hs = [%s] / 1000;" % ", ".join(["hs" + str(i) for i in range(1, end)]))
    # print("tf = [%s] / 1000;" % ", ".join(["tf" + str(i) for i in range(1, end)]))
    # print(
    #     'groups1 = [%s];' % ", ".join(["zeros(1, %d) + %d" % (len(handshake_latencies[i]), i) for i in range(1, end)]))
    # print('groups2 = [%s];' % ", ".join(
    #     ["zeros(1, %d) + %d" % (len(handshake_latencies[i]), i + end) for i in range(1, end)]))
    # print('positions = [%s];' % str((list(range(1, end)) + [i + 0.25 for i in range(1, end)])))
    # print("f = boxplot([hs tf], [groups1 groups2], 'positions', positions);")
    # print("set(f, 'xtick', %s)" % ([i + 0.125 for i in range(1, end)]))
    # print("set(f, 'xticklabel', %s)" % ([str(i) for i in range(1, end)]))
    # # print("print('figures/direct-latency','-depsc');")
    print('hs = %s / 1000;' % str([percentile(handshake_latencies[i], 50) for i in range(1, end)]))
    print('tf = %s / 1000;' % str([percentile(transfer_latencies[i], 50) for i in range(1, end)]))
    print('bar([hs; tf]\');')


def main():
    latency()


if __name__ == '__main__':
    main()
