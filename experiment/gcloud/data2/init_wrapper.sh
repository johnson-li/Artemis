#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
root=~/data2
date > ${root}/init_wrapper.sh.start_ts

sudo apt-get update
sudo apt-get install -y tmux

tmux has-session -t init 2> /dev/null; if [[ $? == 0 ]]; then tmux kill-session -t init; fi
tmux new-session -ds init
for i in `seq 4`
do
    tmux new-window -t init:${i}
done

tmux send-key -t init:0 "${root}/init.sh" Enter

date > ${root}/init_wrapper.sh.end_ts
