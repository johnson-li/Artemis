iname="$(ip -o link show | sed -rn '/^[0-9]+: en/{s/.: ([^:]*):.*/\1/p}')"

sudo useradd -m johnson && echo "johnson:johnson" | chpasswd && adduser johnson sudo
sudo apt-get update -qq
sudo apt-get install -y -qq net-tools openssh-server sudo zsh git vim
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers
chsh -s "$(which zsh)" johnson
sudo su johnson -c 'mkdir /home/johnson/.ssh'
sudo su johnson -c 'echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDVcYOl/Q/TkpxdA4GYbVda8flEQ3EDTaNoBMzYHQ/owPYXP/vaAT3DL3Lxgs12eslNA9px8wqNckmdUdc0NsUyh8Od1ke2S+FCkC/b2tK75aZ3PQsGJb0z+hdYu1/kFby5WKllTQRgNkvkOhTOWu+ybFeiCrylShMXXrkdC6aBQ8w7qWyaGlr1CBs+cKxAd2zyuYn3E5KiyhJPFZr+hN8EH6Q0wtAwTec8ViosY7pEcdIkBl1RUvwiZdaCv5fnGoax62dzQO7jCTVdBAH3jQifBsMLaLffGKqGjF926DLFwhEpUEKL4B/I3LNehAbV+xDnIkFchucgjNkmXamv5yl7W5PVgdyl3W7SoxKfVut0/0eKUKjRplZrhKVCRNLKqnHA9C3yF8QAYRwhlAOwFarEAi5zJNJV+JniFpNkXCsXdJxuZukHPDVJlY8LVyopxbvjSGTowlwgIoCtJPWbW15nioo0Sm1exVJff50eG6L8oTbFTCIar2YcXz07skqmW1nqE53bEBgqageSsjOcBouS8f7X3xOC66qQB1Oyyi9+gUJF4O6NpLlhFvyJMER3Yl4v89LyqAUi27FGbcn+zzCKELV5zjHTmJ+18EOPYv8h7IIJ4nR31QCD4F1eW1TRt4fXn8oEW/H9H+ItcDKQwSn39ZyK/q1t8hYDV1rzavv59w== johnsonli1993@gmail.com" > /home/johnson/.ssh/authorized_keys'
sudo su johnson -c 'wget -q https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true'
sudo su johnson -c 'ln -s /home/vagrant/app /home/johnson/app'
sudo su johnson -c "echo 'export PATH=$PATH:/sbin' >> /home/johnson/.zshrc"
echo "export interface=$iname" | sudo tee -a /etc/environment > /dev/null
