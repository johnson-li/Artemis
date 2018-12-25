interface=`route |grep default| head -n1| tr -s ' '| cut -d' ' -f8`
./compile.sh
sudo ./balancer ${interface}
