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

## Start hosts
1. `python3 -m hestia.start_up`

## Init servers
1. `PYTHONPATH=../ fab init`
1. `PYTHONPATH=../ fab clear_gre`
1. `PYTHONPATH=../ fab setup_gre`
1. `PYTHONPATH=../ fab clear_flows`
1. `python3 -m hestia.tools.setup_dns`
1. `PYTHONPATH=../ fab start_servers`

## Setup routes
1. `python3 -m hestia.experiment.main`

## Run clients
1. `./prepare_and_run.sh plt_host`

## Stop hosts and release resources
1. `python3 -m hestia.clean_up`
