date >~/init.sh.start_ts

sudo debconf-set-selections <<<'mysql-server mysql-server/root_password password root'
sudo debconf-set-selections <<<'mysql-server mysql-server/root_password_again password root'

iname="$(ip -o link show | sed -rn '/^[0-9]+: en/{s/.: ([^:]*):.*/\1/p}')"

id johnson >/dev/null 2>&1 || sudo useradd -m johnson && echo "johnson:johnson" | sudo chpasswd && sudo adduser johnson sudo >/dev/null
sudo DEBIAN_FRONTEND=noninteractive apt-get update -qq
sudo mv /var/lib/dpkg/info/install-info.postinst /var/lib/dpkg/info/install-info.postinst.bad  # fix for apt install info error
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-downgrades -qq apache2 net-tools openssh-server git vim tmux openvswitch-switch iputils-ping libev-dev mysql-server libmysqlclient20=5.7.21-1ubuntu1 libmysqlclient-dev=5.7.21-1ubuntu1 jq expect python-openvswitch python-netifaces
sudo DEBIAN_FRONTEND=noninteractive apt-get --fix-broken install -y -qq
sudo pip3 install mysqlclient >/dev/null 2>&1
echo 'sudo ALL=(ALL) NOPASSWD:ALL' | sudo tee -a /etc/sudoers >/dev/null
sudo su johnson -c 'mkdir -p /home/johnson/.ssh'
sudo su johnson -c 'echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDVcYOl/Q/TkpxdA4GYbVda8flEQ3EDTaNoBMzYHQ/owPYXP/vaAT3DL3Lxgs12eslNA9px8wqNckmdUdc0NsUyh8Od1ke2S+FCkC/b2tK75aZ3PQsGJb0z+hdYu1/kFby5WKllTQRgNkvkOhTOWu+ybFeiCrylShMXXrkdC6aBQ8w7qWyaGlr1CBs+cKxAd2zyuYn3E5KiyhJPFZr+hN8EH6Q0wtAwTec8ViosY7pEcdIkBl1RUvwiZdaCv5fnGoax62dzQO7jCTVdBAH3jQifBsMLaLffGKqGjF926DLFwhEpUEKL4B/I3LNehAbV+xDnIkFchucgjNkmXamv5yl7W5PVgdyl3W7SoxKfVut0/0eKUKjRplZrhKVCRNLKqnHA9C3yF8QAYRwhlAOwFarEAi5zJNJV+JniFpNkXCsXdJxuZukHPDVJlY8LVyopxbvjSGTowlwgIoCtJPWbW15nioo0Sm1exVJff50eG6L8oTbFTCIar2YcXz07skqmW1nqE53bEBgqageSsjOcBouS8f7X3xOC66qQB1Oyyi9+gUJF4O6NpLlhFvyJMER3Yl4v89LyqAUi27FGbcn+zzCKELV5zjHTmJ+18EOPYv8h7IIJ4nR31QCD4F1eW1TRt4fXn8oEW/H9H+ItcDKQwSn39ZyK/q1t8hYDV1rzavv59w== johnsonli1993@gmail.com" > /home/johnson/.ssh/authorized_keys'
sudo su johnson -c "echo 'export PATH=$PATH:/sbin' >> /home/johnson/.bashrc"
echo "export interface=$iname" | sudo tee -a /etc/environment >/dev/null

hostname=$(hostname)
server_id=$(python3 -c 'import json; machines=json.load(open("machine.json")); split_ip=machines[machines["hostname"]]["internal_ip1"].split("."); print(split_ip[3])')

grep -q "mysqld" /etc/mysql/my.cnf
if [ $? -ne 0 ]; then
  sudo sh -c 'echo "\n[mysqld]\nlog-bin=mysql-bin\nserver-id=\c" >> /etc/mysql/my.cnf'
  sudo sh -c "echo $server_id >> /etc/mysql/my.cnf"
else
  sudo sed -i "/server-id=/c\server-id=${server_id}" /etc/mysql/my.cnf
fi

position=$(python3 -c 'import json; machines=json.load(open("machine.json"));pos=machines["position"]; print(pos)')
fl=$(python3 -c 'import json; machines=json.load(open("machine.json"));f=machines["file"]; print(f)')
fl="'"$fl"'"

sudo service mysql restart
export MYSQL_PWD=root
mysql -uroot -e "stop slave;"
mysql -uroot -e "change master to \
  master_host='35.228.34.228', \
  master_user='slave', \
  master_password='123456', \
  master_log_file=$fl, \
  master_log_pos=$position;"
mysql -uroot -e "start slave;"

sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
sudo service apache2 restart
echo "$hostname" | sudo tee /var/www/html/index.html >/dev/null

date >~/init.sh.end_ts

~/data2/setup.sh

~/data2/init_db.sh
