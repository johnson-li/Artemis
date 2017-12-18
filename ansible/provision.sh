#!/usr/bin/env bash

export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i inventory/hosts.yml provision.yml