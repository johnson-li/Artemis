import MySQLdb
import os
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from hestia import PROJECT_PATH

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Helvetica']
DATA_PATH = os.path.join(PROJECT_PATH, f'experiment/data')
FONT_SIZE = 16
CLIENT_REGIONS = ['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1',
                  'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3',
                  'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']


def decode(i):
    e = i
    if type(i) is bytes:
        e = i.decode('utf-8')
    elif type(i) is str:
        try:
            e = float(i)
            e = int(i)
        except Exception as _:
            pass
    return e


def shorten(a):
    a = a[7:]
    return '-'.join([''.join((t[:2], t[-2:])) for t in a.split('-')[:2]])


def handle_region(name, last=False):
    latencies = {}
    db = MySQLdb.connect("127.0.0.1", "johnson", "johnson", "serviceid_db")
    db.query('select * from measurements order by ts')
    client_ip_mapping = {}
    r = db.store_result()
    while True:
        a = r.fetch_row()
        if not a:
            break
        a = a[0]
        _, server_region, client_ip, latency, _ = a
        latencies.setdefault(client_ip, {})[server_region] = latency
    db.query('select * from transfer_time')
    r = db.store_result()
    data = {}
    anycast_targets = {}
    while True:
        a = r.fetch_row()
        if not a:
            break
        a = a[0]
        item_id, client_ip, router_ip, server_ip, hostname, client_region, router_region, server_region, \
        service_id_transfer_time, service_id_handshake_time, dns_query_time, dns_transfer_time, \
        dns_handshake_time, anycast_transfer_time, anycast_handshake_time, service_plt_time, dns_plt_time, \
        anycast_plt_time, bind_server_ip, website, timestamp = [decode(i) for i in a]
        client_ip_mapping[client_ip] = client_region
        anycast_targets[client_region] = '-'.join([''.join((t[:2], t[-2:])) for t in router_region[7:].split('-')[:2]])
        data.setdefault(client_ip, {'hostname': hostname, 'client_region': client_region, 'records': []})
        data[client_ip]['records'].append({'router_ip': router_ip, 'server_ip': server_ip,
                                           'router_region': router_region, 'server_region': server_region,
                                           'sid_tf': service_id_transfer_time, 'sid_hs': service_id_handshake_time,
                                           'dns_query': dns_query_time, 'dns_tf': dns_transfer_time,
                                           'dns_hs': dns_handshake_time,
                                           'any_tf': anycast_transfer_time, 'any_hs': anycast_handshake_time,
                                           'sid_plt': service_plt_time, 'dns_plt': dns_plt_time,
                                           'any_plt': anycast_plt_time, 'bind_server_ip': bind_server_ip,
                                           'website': website, 'timestamp': timestamp})
    latencies = {client_ip_mapping[k]: v for k, v in latencies.items()}
    anycast_additional_latency = {k: (latencies[k][anycast_targets[k]] -
                                      np.min(list(latencies[k].values()))) / 1
                                  for k in latencies.keys()}
    print(anycast_additional_latency)
    print(f'Anycast additional latency: {np.mean(list(anycast_additional_latency.values()))}')
    statics = np.median
    statics2 = np.mean
    client_ips = []
    for client_region in CLIENT_REGIONS:
        for client_ip, value in data.items():
            if value['client_region'] == client_region:
                client_ips.append(client_ip)
                break
    sid_hs_list = []
    sid_tf_list = []
    dns_query_list = []
    dns_hs_list = []
    dns_tf_list = []
    any_hs_list = []
    any_tf_list = []
    routing_list = []
    x = np.array(range(len(client_ips)))
    for client_ip in client_ips:
        records = data[client_ip]['records']
        routing_list.append(
            [(data[client_ip]['client_region'], shorten(r['router_region']), r['server_region']) for r in records][0])
        sid_hs_list.append(statics([r['sid_hs'] for r in records]) / 1000)
        sid_tf_list.append(statics([r['sid_tf'] for r in records]) / 1000)
        dns_query_list.append(statics2([r['dns_query'] for r in records]))
        dns_hs_list.append(statics([r['dns_hs'] for r in records]) / 1000)
        dns_tf_list.append(statics([r['dns_tf'] for r in records]) / 1000)
        any_hs_list.append(statics([r['any_hs'] for r in records]) / 1000)
        any_tf_list.append(statics([r['any_tf'] for r in records]) / 1000)
    sid_hs_list = np.array(sid_hs_list)
    sid_tf_list = np.array(sid_tf_list)
    dns_query_list = np.array(dns_query_list)
    dns_hs_list = np.array(dns_hs_list)
    dns_tf_list = np.array(dns_tf_list)
    any_hs_list = np.array(any_hs_list)
    any_tf_list = np.array(any_tf_list)

    dns_hs_list0 = dns_hs_list.copy()
    dns_tf_list0 = dns_tf_list.copy()
    dns_hs_list += dns_query_list
    dns_tf_list += dns_query_list
    optimal_flags = np.array([x[1] == x[2] for x in routing_list])
    opt_idx = np.where(optimal_flags)[0]
    subopt_idx = np.where(optimal_flags == False)[0]
    optimal_ratio = len(list(filter(lambda x: x, optimal_flags))) / len(routing_list) * 100
    print(f'Anycast optimal ratio: {optimal_ratio}%')
    anycast_additional_hs = (any_hs_list[subopt_idx] - dns_hs_list0[subopt_idx]) / dns_hs_list0[subopt_idx] * 100
    anycast_additional_tf = (any_tf_list[subopt_idx] - dns_tf_list0[subopt_idx]) / dns_tf_list0[subopt_idx] * 100
    # print(f'Anycast additional handshake latency: {np.mean(anycast_additional_hs)}%')
    # print(f'Anycast additional transport latency: {np.mean(anycast_additional_tf)}%')
    print(f'Artemis handshake latency: {np.mean(sid_hs_list)}')
    print(f'Artemis transport latency: {np.mean(sid_tf_list)}')
    print(f'DNS handshake latency: {np.mean(dns_hs_list)}')
    print(f'DNS transport latency: {np.mean(dns_tf_list)}')
    print(f'Anycast handshake latency: {np.mean(any_hs_list)}')
    print(f'Anycast transport latency: {np.mean(any_tf_list)}')



    fig, ax = plt.subplots(figsize=(8, 3))
    width = 0.25
    ax.bar(x - width, sid_tf_list, width, label='Hestia', color='#f2cfa3')
    ax.bar(x - width, sid_hs_list, width,
           label='Hestia', color='#f2cfa3', hatch='////', edgecolor='#a27f53', linewidth=.8)
    ax.bar(x, dns_tf_list, width, label='DNS', color='#e75d56')
    ax.bar(x, dns_hs_list, width,
           label='DNS', color='#e75d56', hatch='////', edgecolor='#970906', linewidth=.8)
    ax.bar(x, dns_query_list, width, label='DNS', color='#bc5090')
    ax.bar(x + width, any_tf_list, width, label='Anycast', color='#aee1f4')
    ax.bar(x + width, any_hs_list, width,
           label='Anycast', color='#aee1f4', hatch='////', edgecolor='#5e91a4', linewidth=.8)
    ax.tick_params(axis='both', which='major', labelsize=FONT_SIZE - 2)
    plt.gca().set_ylim(bottom=0)
    plt.xticks(range(len(client_ips)), range(1, len(client_ips) + 1))
    plt.xlabel('AWS clients', fontsize=FONT_SIZE)
    plt.ylabel('Latency (ms)', fontsize=FONT_SIZE)
    plt.ylim(0, 250)
    if last:
        ax.legend(fontsize=FONT_SIZE - 6, handles=[mpatches.Patch(color='#f2cfa3', label='Hestia'),
                                                   mpatches.Patch(color='#e75d56', label='DNS'),
                                                   mpatches.Patch(color='#aee1f4', label='Anycast'),
                                                   mpatches.Patch(color='#bc5090', label='DNS query latency'),
                                                   mpatches.Patch(facecolor='#ffffff', label='Transport latency',
                                                                  edgecolor='#888888'),
                                                   mpatches.Patch(facecolor='#ffffff', label='Handshake latency',
                                                                  hatch='////', edgecolor='#888888'),
                                                   ])
    fig.tight_layout()
    # plt.savefig(os.path.join(DATA_PATH, f'{name}.pdf'),
    #             format='pdf', dpi=1000, bbox_inches='tight')
    # plt.show()


def main():
    files = (('dump_global_large.sql', 'global_large'), ('dump_global_small.sql', 'global_small'),
             ('dump_regional_europe.sql', 'regional_europe'), ('dump_regional_us.sql', 'regional_us'))
    files = [files[2]]
    for file_name, name in files:
        os.system(f'mysql -pjohnson serviceid_db < {os.path.join(DATA_PATH, file_name)}')
        handle_region(name, name == 'regional_us')


if __name__ == '__main__':
    main()
