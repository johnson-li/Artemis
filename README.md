Artemis: A Latency-Oriented Naming and Routing System
===
[Artemis](https://ieeexplore.ieee.org/document/9894091) is a novel naming and routing system. It supports DNS-like name resolution but is of lower latency. It provides a global service discovery solution.

Authors: [Xuebing Li](https://github.com/johnson-li)
, [Yang Chen](https://github.com/chenyang03), [Mengying Zhou](https://github.com/mengyingzhou), [Tiancheng Guo](https://github.com/skyerguo), Chenhao Wang, Yu Xiao, Junjie Wan, and Xin Wang

## Abstract


Today, Internet service deployment is typically implemented with server replication at multiple locations. Domain name system (DNS), which translates human-readable domain names into network-routable IP addresses, is typically used for distributing users to different server replicas. However, DNS relies on several network-based queries and the queries delay the connection setup process between the client and the server replica. In this paper, we propose Artemis, a practical low-latency naming and routing system that supports optimal server (replica) selection based on user-defined policies and provides lower query latencies than DNS. Artemis uses a DNS-like domain name-IP mapping for replica selection and achieves low query latency by combining the name resolution process with the transport-layer handshake process. In Artemis, all of the server replicas at different locations share the same anycast IP address, called Service Address. Clients use the Service Address to establish a transport-layer connection with the server. The client’s initial handshake packet is routed over an overlay network to reach the optimal server. Then the server migrates the transport layer connection to its original unicast IP address after finishing the handshake process. After that, service discovery is completed, and the client communicates with the server directly via IP addresses. To validate the effectiveness of Artemis, we evaluate its performance via both real trace-driven simulation and real-world deployment. The result shows that Artemis can handle a large number of connections and reduce the connection setup latency compared with state-of-the-art solutions. More specifically, our deployment across 11 Google data centers shows that Artemis reduces the connection setup latency by 39.4% compared with DNS.

![Artemis Architecture](/docs/images/artemis_architecture.png)


This repo contains the Artemis code, the deployment and evaluation scripts, and the data collected during the evaluation.




Cloud Evaluation Setup
===

## Topology

See [this doc](docs/topology.md).

## Evaluation Steps


### Start OVS controller
1. `java -jar target/floodlight.jar`

### Start hosts
1. `python3 -m hestia.start_up`
1. `python3 -m hestia.tools.generate_hosts`
1. `python3 -m hestia.tools.setup_dns`

### Init servers
1. `PYTHONPATH=../ fab init_nic`
1. `PYTHONPATH=../ fab init_ovs`
1. `PYTHONPATH=../ fab clear_gre`
1. `PYTHONPATH=../ fab setup_gre`
1. `PYTHONPATH=../ fab clear_flows`
1. `PYTHONPATH=../ fab start_servers`

### Setup routes
1. `python3 -m hestia.experiment.main`

### Run clients
1. `python3 -m hestia.plt.main`

### Stop hosts and release resources
1. `python3 -m hestia.clean_up`

### Refresh planetlab hosts
1. `python3 -m hestia.tools.available_plt_hosts`

### QUIC implementation
A customized QUIC implementation is required to run this project. Please refer to https://github.com/johnson-li/ngtcp2. 

License
===

This project is released under the MIT license. Please see the [LICENSE](/docs/LICENSE) file for more information.



Cite the project 
===
```
@article{artemis,
  author  = {Xuebing Li and Yang Chen and Mengying Zhou and Tiancheng Guo and Chenhao Wang and Yu Xiao and Junjie Wan and Xin Wang},
  title   = {Artemis: A Latency-Oriented Naming and Routing System},
  journal = {IEEE Transactions on Parallel and Distributed Systems},
  year    = {2022},
}
```
