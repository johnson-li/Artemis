#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
root=/tmp/hestia/data
date > ${root}/start_wrapper.sh.start_ts

tmux has-session -t main 2> /dev/null; if [[ $? == 0 ]]; then tmux kill-session -t main; fi
tmux new-session -ds main
for i in `seq 4`
do
    tmux new-window -t main:${i}
done

tmux send-key -t main:0 "export region=$region" Enter
tmux send-key -t main:0 "export lb_ip=$lb_ip" Enter
tmux send-key -t main:0 "${root}/start.sh" Enter

date > ${root}/start_wrapper.sh.end_ts

