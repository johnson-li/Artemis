#!/usr/bin/env bash

tmux has-session -t benchmark 2> /dev/null; if [[ $? == 0 ]]; then tmux kill-session -t benchmark; fi
tmux new-session -ds benchmark
for i in `seq 5`
do
    tmux new-window -t benchmark:${i}
done

tmux send-key -t benchmark:0 'cd /home/lix16/Workspace/ngtcp2' Enter
tmux send-key -t benchmark:1 'cd /home/lix16/Workspace/Hestia' Enter

if [[ -n "$provision" ]]; then
    tmux send-key -t benchmark:1 'source ./.venv/bin/activate; pip install --upgrade pip; pip install -qr requirements.txt; python -m hestia.system.main' Enter
    sleep 60
fi


echo 'benchmark for direct connections'
tmux send-key -t benchmark:0 'rm -rf ~/data/sid' Enter
tmux send-key -t benchmark:0 'mkdir -p ~/data/sid' Enter
tmux send-key -t benchmark:3 "ssh johnson@173.16.156.101" Enter
sleep 0.5

tmux send-key -t benchmark:3 "tmux send-key -t main:1 'rm -rf ~/data/sid; mkdir -p ~/data/sid' Enter" Enter

for i in `seq 2`
do
    echo "concurrency: $i"
    tmux send-key -t benchmark:3 "tmux send-key -t main:0 C-c" Enter
    tmux send-key -t benchmark:3 "tmux send-key -t main:1 'while true; do ps -eo pcpu,args -q `pidof client`| tail -n1 | cut -d\" \" -f2 >> ~/data/sid/dir-s$i.cpu; done'" Enter
    tmux send-key -t benchmark:3 'tmux send-key -t main:0 "sudo LD_LIBRARY_PATH=$HOME/app/bin ~/app/bin/server --interface=${interface} --unicast=${unicast} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert"' Enter
    sleep 0.5
    tmux send-key -t benchmark:2 "while true; do ps -eo pcpu,args -q `pidof client`| tail -n1 | cut -d' ' -f2 >> ~/data/sid/dir-c$i.cpu; done" Enter
    tmux send-key -t benchmark:0 "./examples/client --concurrency=$i --timeout=1 --remote=173.16.156.101 site1.xuebingli.com 4433 2>&1|stdbuf -o0 grep 'time: ' >> ~/data/sid/dir-c$i.log" Enter
    sleep 10
    tmux send-key -t benchmark:2 C-c
    tmux send-key -t benchmark:3 "tmux send-key -t main:0 C-c" Enter
    tmux send-key -t benchmark:2 "sudo pmap `pidof client`| tail -n1| egrep -o '[0-9]+' > ~/data/sid/dir-c$i.mem" Enter
    tmux send-key -t benchmark:3 "tmux send-key -t main:1 C-c" Enter
    tmux send-key -t benchmark:3 "tmux send-key -t main:1 \"sudo pmap `pidof server`| tail -n1| egrep -o '[0-9]+' > ~/data/sid/dir-s$i.mem\"" Enter
done

echo 'benchmark for artemis connections with one hop'

echo 'benchmark for artemis connections with two hops'

