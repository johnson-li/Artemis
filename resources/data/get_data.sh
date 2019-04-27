#!/usr/bin/env bash

ssh workstation-br "scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no johnson@173.16.156.100:'~/data/sid/*' ~/data/sid"
ssh workstation-br "scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no johnson@173.16.156.101:'~/data/sid/*' ~/data/sid"
ssh workstation-br "scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no johnson@173.16.156.150:'~/data/sid/*' ~/data/sid"
rsync -r workstation-br:"~/data/sid" .