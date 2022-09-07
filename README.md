Hestia
===
Use AWS API to setup the experiment environment.


Topology
===
See [this doc](docs/topology.md).


Configuration
===

Steps
===

## Start OVS controller
1. `java -jar target/floodlight.jar`

## Start hosts
1. `python3 -m hestia.start_up`
1. `python3 -m hestia.tools.generate_hosts`
1. `python3 -m hestia.tools.setup_dns`

## Init servers
1. `PYTHONPATH=../ fab init_nic`
1. `PYTHONPATH=../ fab init_ovs`
1. `PYTHONPATH=../ fab clear_gre`
1. `PYTHONPATH=../ fab setup_gre`
1. `PYTHONPATH=../ fab clear_flows`
1. `PYTHONPATH=../ fab start_servers`

## Setup routes
1. `python3 -m hestia.experiment.main`

## Run clients
1. `python3 -m hestia.plt.main`

## Stop hosts and release resources
1. `python3 -m hestia.clean_up`

## Refresh planetlab hosts
1. `python3 -m hestia.tools.available_plt_hosts`

## Cite the project 
```
@article{artemis,
  author  = {Xuebing Li and Yang Chen and Mengying Zhou and Tiancheng Guo and Chenhao Wang and Yu Xiao and Junjie Wan and Xin Wang},
  title   = {Artemis: A Latency-Oriented Naming and Routing System},
  journal = {IEEE Transactions on Parallel and Distributed Systems},
  year    = {2022},
}
```
