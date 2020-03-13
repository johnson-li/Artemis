date > ~/init.sh.start_ts

sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root';
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root';

iname="$(ip -o link show | sed -rn '/^[0-9]+: en/{s/.: ([^:]*):.*/\1/p}')"

id johnson > /dev/null 2>&1 || sudo useradd -m johnson && echo "johnson:johnson" | sudo chpasswd && sudo adduser johnson sudo > /dev/null
sudo DEBIAN_FRONTEND=noninteractive apt-get update -qq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq net-tools openssh-server sudo git vim tmux openvswitch-switch pkg-config iputils-ping libev-dev mysql-client mysql-server python3-dev python3-pip libmysqlclient-dev jq libmariadbclient18 expect
sudo DEBIAN_FRONTEND=noninteractive apt-get --fix-broken install -y -qq
sudo pip3 install mysqlclient > /dev/null 2>&1
echo 'sudo ALL=(ALL) NOPASSWD:ALL' | sudo tee -a /etc/sudoers > /dev/null
sudo su johnson -c 'mkdir -p /home/johnson/.ssh'
sudo su johnson -c 'echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDVcYOl/Q/TkpxdA4GYbVda8flEQ3EDTaNoBMzYHQ/owPYXP/vaAT3DL3Lxgs12eslNA9px8wqNckmdUdc0NsUyh8Od1ke2S+FCkC/b2tK75aZ3PQsGJb0z+hdYu1/kFby5WKllTQRgNkvkOhTOWu+ybFeiCrylShMXXrkdC6aBQ8w7qWyaGlr1CBs+cKxAd2zyuYn3E5KiyhJPFZr+hN8EH6Q0wtAwTec8ViosY7pEcdIkBl1RUvwiZdaCv5fnGoax62dzQO7jCTVdBAH3jQifBsMLaLffGKqGjF926DLFwhEpUEKL4B/I3LNehAbV+xDnIkFchucgjNkmXamv5yl7W5PVgdyl3W7SoxKfVut0/0eKUKjRplZrhKVCRNLKqnHA9C3yF8QAYRwhlAOwFarEAi5zJNJV+JniFpNkXCsXdJxuZukHPDVJlY8LVyopxbvjSGTowlwgIoCtJPWbW15nioo0Sm1exVJff50eG6L8oTbFTCIar2YcXz07skqmW1nqE53bEBgqageSsjOcBouS8f7X3xOC66qQB1Oyyi9+gUJF4O6NpLlhFvyJMER3Yl4v89LyqAUi27FGbcn+zzCKELV5zjHTmJ+18EOPYv8h7IIJ4nR31QCD4F1eW1TRt4fXn8oEW/H9H+ItcDKQwSn39ZyK/q1t8hYDV1rzavv59w== johnsonli1993@gmail.com" > /home/johnson/.ssh/authorized_keys'
sudo su johnson -c "echo 'export PATH=$PATH:/sbin' >> /home/johnson/.bashrc"
echo "export interface=$iname" | sudo tee -a /etc/environment > /dev/null

sudo sh -c 'echo "\n[mysqld]\nlog-bin=mysql-bin\nserver-id=2" >> /etc/mysql/my.cnf'
sudo service mysql restart
export MYSQL_PWD=root
mysql -uroot -e "stop slave;"
mysql -uroot -e 'change master to \
	master_host="10.146.0.2", \
	master_user="slave", \
	master_password="123456", \
	master_log_file="mysql-bin.000005", \
	master_log_pos=327;'
mysql -uroot -e "start slave;"

date > ~/init.sh.end_ts

~/data/setup.sh

~/data/init_db.sh

