#!/usr/bin/env bash

source ~/env

if [[ -z "$interface" ]]
then
    interface=`route |grep default| head -n1| tr -s ' '| cut -d' ' -f8`
fi

sudo killall balancer 2> /dev/null
sudo killall server 2> /dev/null
sudo killall python3 2> /dev/null

tmux has-session -t main 2> /dev/null; if [[ $? == 0 ]]; then tmux kill-session -t main; fi
tmux new-session -ds main
for i in `seq 2`
do
    tmux new-window -t main:${i}
done

case ${ROLE} in
    "balancer")
        tmux send-key -t main:0 'source ~/env'
        tmux send-key -t main:0 'sudo LD_LIBRARY_PATH=$HOME/app/bin ~/app/bin/balancer --datacenter=${DATACENTER} --mysql=${DATABASE} --user=johnson --password="welcOme0\!" ${interface} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert' Enter
        tmux send-key -t main:1 'source ~/env'
        tmux send-key -t main:1 'sudo PYTHONPATH="$HOME/app/" python3 -m hestia.exec.measurement-server ${DATACENTER} ${DATABASE}' Enter
        ;;
    "server")
        tmux send-key -t main:0 'source ~/env'
        tmux send-key -t main:0 'sudo LD_LIBRARY_PATH="$HOME/app/bin" ~/app/bin/server --interface=${interface} --unicast=${unicast} 0.0.0.0 4433 ~/app/keys/server.key ~/app/keys/server.cert' Enter
   ;;
esac
