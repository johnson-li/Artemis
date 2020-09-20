from MySQLdb import _mysql
import os
import numpy as np
import matplotlib.pyplot as plt
from hestia import MATLAB_PATH

from pprint import pprint


def decode(i):
    e = i
    if type(i) is bytes:
        e = i.decode('utf-8')
    else:
        try:
            e = float(i)
            e = int(i)
        except Exception as e:
            pass
    return e


def main():
    db = _mysql.connect("35.228.34.228", "johnson", "johnson", "serviceid_db")
    db.query('select * from transfer_time')
    r = db.store_result()
    data = {}
    while True:
        a = r.fetch_row()
        if not a:
            break
        a = a[0]
        item_id, client_ip, router_ip, server_ip, hostname, client_region, router_region, server_region, \
            service_id_transfer_time, service_id_handshake_time, dns_query_time, dns_transfer_time, \
            dns_handshake_time, anycast_transfer_time, anycast_handshake_time, service_plt_time, dns_plt_time, \
            anycast_plt_time, bind_server_ip, website, timestamp = [decode(i) for i in a]
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
    statics = np.median
    client_ips = list(data.keys())
    sid_hs_list = []
    sid_tf_list = []
    dns_query_list = []
    dns_hs_list = []
    dns_tf_list = []
    any_hs_list = []
    any_tf_list = []
    for client_ip in client_ips:
        records = data[client_ip]['records']
        routing = [(r['router_region'], r['server_region']) for r in records][0]
        sid_hs_list.append(statics([r['sid_hs'] for r in records]) / 1000)
        sid_tf_list.append(statics([r['sid_tf'] for r in records]) / 1000)
        dns_query_list.append(statics([r['dns_query'] for r in records]))
        dns_hs_list.append(statics([r['dns_hs'] for r in records]) / 1000)
        dns_tf_list.append(statics([r['dns_tf'] for r in records]) / 1000)
        any_hs_list.append(statics([r['any_hs'] for r in records]) / 1000)
        any_tf_list.append(statics([r['any_tf'] for r in records]) / 1000)

    matlab_file = os.path.join(MATLAB_PATH, "overall_cmp.m")
    with open(matlab_file, 'w') as f:
        f.write(f'sid_hs = [{", ".join([str(i) for i in sid_hs_list])}];\n')
        f.write(f'sid_tf = [{", ".join([str(i) for i in sid_tf_list])}];\n')
        f.write(f'dns_query = [{", ".join([str(i) for i in dns_query_list])}];\n')
        f.write(f'dns_hs = [{", ".join([str(i) for i in dns_hs_list])}];\n')
        f.write(f'dns_tf = [{", ".join([str(i) for i in dns_tf_list])}];\n')
        f.write(f'any_hs = [{", ".join([str(i) for i in any_hs_list])}];\n')
        f.write(f'any_tf = [{", ".join([str(i) for i in any_tf_list])}];\n')
        f.write('figure();\n')
        f.write('hold on;\n')
        f.write('set(gca,\'FontSize\',18);\n')
        f.write('xlabel("AWS regions");\n')
        f.write('ylabel("Latencies (ms)");\n')
        f.write('bar([sid_tf; dns_tf; any_tf].\', 0.9, \'FaceColor\', [0 0 1]);\n')
        f.write('bar([sid_hs; dns_hs; any_hs].\', 0.5, \'FaceColor\', [0 1 0]);\n')
    # print(np.array(dns_hs_list) - np.array(sid_hs_list))
    print(dns_hs_list)
    print(sid_hs_list)


if __name__ == '__main__':
    main()
