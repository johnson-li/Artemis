#!/usr/bin/env bash

#case ${ROLE} in
#    "balancer")
#        interface=`route |grep default| head -n1| tr -s ' '| cut -d' ' -f8`
#        sudo -b LD_LIBRARY_PATH="$HOME/app/bin" ~/app/bin/balancer ${interface} 127.0.0.1 4433 ~/app/keys/server.key ~/app/keys/server.cert > $HOME/balancer.log 2>&1
#        echo `ps --ppid $! -o pid=` >> $HOME/balancer.pid
#        ;;
#    "server")
#        sudo -b LD_LIBRARY_PATH="$HOME/app/bin" ~/app/bin/server 127.0.0.1 4433 ~/app/keys/server.key ~/app/keys/server.cert > $HOME/server.log 2>&1
#        echo `ps --ppid $! -o pid=` >> $HOME/server.pid
#        ;;
#esac

sudo /usr/sbin/sshd -D

