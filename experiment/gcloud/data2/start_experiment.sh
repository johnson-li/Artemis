date > ~/start_experiment.sh.start_ts

tmux has-session -t main 2> /dev/null; if [[ $? == 0  ]]; then tmux kill-session -t main; fi
tmux new-session -ds main
for i in $(seq 4)
do
    tmux new-window -t main:"$i"
done

tmux send-key -t main:0 '~/data2/start_balancer.sh' Enter
tmux send-key -t main:1 '~/data2/start_server.sh' Enter
tmux send-key -t main:2 'mysql -ujohnson -pjohnson serviceid_db' Enter

date > ~/start_experiment.sh.end_ts
