#!/usr/bin/env bash

concurrency=100

git pull

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
tmux send-key -t benchmark:4 "ssh johnson@173.16.156.100" Enter
tmux send-key -t benchmark:5 "ssh johnson@173.16.156.150" Enter
sleep 0.5

tmux send-key -t benchmark:3 "tmux send-key -t main:1 'rm -rf ~/data/sid; mkdir -p ~/data/sid' Enter" Enter
tmux send-key -t benchmark:4 "tmux send-key -t main:1 'rm -rf ~/data/sid; mkdir -p ~/data/sid' Enter" Enter
tmux send-key -t benchmark:5 "tmux send-key -t main:1 'rm -rf ~/data/sid; mkdir -p ~/data/sid' Enter" Enter
sleep 0.5

for i in `seq ${concurrency}`
do
    echo "concurrency: $i"
    tmux send-key -t benchmark:3 "tmux send-key -t main:0 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:1 '"'"'while true; do ps -eo pcpu,args -q `pidof server` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/dir-s'${i}'.cpu; done'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:0 '"'"'sudo LD_LIBRARY_PATH=$HOME/app/bin ~/app/bin/server --interface=${interface} --unicast=${unicast} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert'"'"' Enter' Enter
    sleep 1
    tmux send-key -t benchmark:2 'while true; do ps -eo pcpu,args -q `pidof client` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/dir-c'${i}'.cpu; done' Enter
    sleep .1
    tmux send-key -t benchmark:0 C-c
    sleep .1
    tmux send-key -t benchmark:0 "./examples/client --concurrency=$i --timeout=1 --remote=173.16.156.101 site1.xuebingli.com 4433 2>&1|stdbuf -o0 grep 'time: ' >> ~/data/sid/dir-c$i.log" Enter
    sleep 3
    tmux send-key -t benchmark:2 C-c
    sleep .1
    tmux send-key -t benchmark:2 'sudo pmap `pidof client`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/dir-c'${i}'.mem' Enter
    sleep .1
    tmux send-key -t benchmark:3 "tmux send-key -t main:1 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:2 '"'"'sudo pmap `pidof server`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/dir-s'${i}'.mem'"'"' Enter' Enter
    sleep 1
done

echo 'benchmark for artemis connections with one hop'
for i in `seq ${concurrency}`
do
    echo "concurrency: $i"
    tmux send-key -t benchmark:3 "tmux send-key -t main:0 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:4 "tmux send-key -t main:0 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:1 '"'"'while true; do ps -eo pcpu,args -q `pidof server` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/ar1-s'${i}'.cpu; done'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:4 'tmux send-key -t main:1 '"'"'while true; do ps -eo pcpu,args -q `pidof balancer` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/ar1-b'${i}'.cpu; done'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:0 '"'"'sudo LD_LIBRARY_PATH=$HOME/app/bin ~/app/bin/server --interface=${interface} --unicast=${unicast} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:4 'tmux send-key -t main:0 '"'"'sudo LD_LIBRARY_PATH=$HOME/app/bin ~/app/bin/balancer --datacenter=${DATACENTER} ${interface} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert'"'"' Enter' Enter
    sleep 1
    tmux send-key -t benchmark:2 'while true; do ps -eo pcpu,args -q `pidof client` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/ar1-c'${i}'.cpu; done' Enter
    sleep .1
    tmux send-key -t benchmark:0 C-c
    sleep .1
    tmux send-key -t benchmark:0 "./examples/client --concurrency=$i --timeout=1 --remote=170.16.156.100 site1.xuebingli.com 4433 2>&1|stdbuf -o0 grep 'time: ' >> ~/data/sid/ar1-c$i.log" Enter
    sleep 3
    tmux send-key -t benchmark:2 C-c
    sleep .1
    tmux send-key -t benchmark:2 'sudo pmap `pidof client`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/ar1-c'${i}'.mem' Enter
    sleep .1
    tmux send-key -t benchmark:3 "tmux send-key -t main:1 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:4 "tmux send-key -t main:1 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:2 '"'"'sudo pmap `pidof server`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/ar1-s'${i}'.mem'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:4 'tmux send-key -t main:2 '"'"'sudo pmap `pidof balancer`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/ar1-b'${i}'.mem'"'"' Enter' Enter
    sleep 1
done


echo 'benchmark for artemis connections with two hops'
tmux send-key -t benchmark:4 'sudo ovs-ofctl add-flow bridge priority=65535,in_port=`sudo ovs-vsctl -- --columns=name,ofport list Interface tsv0| tail -n1| egrep -o "[0-9]+"`,actions=mod_nw_src:170.16.156.150,mod_dl_dst:`ping -c1 170.16.156.1 > /dev/null; arp| grep "170.16.156.1 "| egrep -o "[0-9a-z:]{12,}"`,`sudo ovs-vsctl -- --columns=name,ofport list Interface enp0s8| tail -n1| egrep -o "[0-9]+"`' Enter
sleep .1
for i in `seq ${concurrency}`
do
    echo "concurrency: $i"
    tmux send-key -t benchmark:3 "tmux send-key -t main:0 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:4 "tmux send-key -t main:0 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:1 '"'"'while true; do ps -eo pcpu,args -q `pidof server` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/ar2-s'${i}'.cpu; done'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:4 'tmux send-key -t main:1 '"'"'while true; do ps -eo pcpu,args -q `pidof balancer` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/ar2-ba'${i}'.cpu; done'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:5 'tmux send-key -t main:1 '"'"'while true; do ps -eo pcpu,args -q `pidof balancer` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/ar2-bb'${i}'.cpu; done'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:0 '"'"'sudo LD_LIBRARY_PATH=$HOME/app/bin ~/app/bin/server --interface=${interface} --unicast=${unicast} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:4 'tmux send-key -t main:0 '"'"'sudo LD_LIBRARY_PATH=$HOME/app/bin ~/app/bin/balancer --datacenter=${DATACENTER} ${interface} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:5 'tmux send-key -t main:0 '"'"'sudo LD_LIBRARY_PATH=$HOME/app/bin ~/app/bin/balancer --datacenter=${DATACENTER} ${interface} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert'"'"' Enter' Enter
    sleep 1
    tmux send-key -t benchmark:2 'while true; do ps -eo pcpu,args -q `pidof client` 2> /dev/null| tail -n1 | cut -d" " -f2 >> ~/data/sid/ar2-c'${i}'.cpu; done' Enter
    sleep .1
    tmux send-key -t benchmark:0 C-c
    sleep .1
    tmux send-key -t benchmark:0 "./examples/client --concurrency=$i --timeout=1 --remote=171.16.156.100 site1.xuebingli.com 4433 2>&1|stdbuf -o0 grep 'time: ' >> ~/data/sid/ar2-c$i.log" Enter
    sleep 3
    tmux send-key -t benchmark:2 C-c
    sleep .1
    tmux send-key -t benchmark:2 'sudo pmap `pidof client`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/ar2-c'${i}'.mem' Enter
    sleep .1
    tmux send-key -t benchmark:3 "tmux send-key -t main:1 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:4 "tmux send-key -t main:1 C-c" Enter
    sleep .1
    tmux send-key -t benchmark:3 'tmux send-key -t main:2 '"'"'sudo pmap `pidof server`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/ar2-s'${i}'.mem'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:4 'tmux send-key -t main:2 '"'"'sudo pmap `pidof balancer`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/ar2-ba'${i}'.mem'"'"' Enter' Enter
    sleep .1
    tmux send-key -t benchmark:5 'tmux send-key -t main:2 '"'"'sudo pmap `pidof balancer`| tail -n1| egrep -o "[0-9]+" > ~/data/sid/ar2-bb'${i}'.mem'"'"' Enter' Enter
    sleep 1
done
