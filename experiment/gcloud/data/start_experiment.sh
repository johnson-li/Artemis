date > ~/start_experiment.sh.start_ts

tmux has-session -t main 2> /dev/null; if [[ $? == 0  ]]; then tmux kill-session -t main; fi
tmux new-session -ds main
for i in `seq 4`
do
    tmux new-window -t main:${i}
done

hostname=`hostname`
role=${hostname:`expr ${#hostname} - 6`:6}
case $role in
    "router")
        tmux send-key -t main:0 '~/data/start_balancer.sh' Enter
        ;;
    "server")
        tmux send-key -t main:0 '~/data/start_server.sh' Enter
        ;;
esac

date > ~/start_experiment.sh.end_ts
