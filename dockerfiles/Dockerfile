FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y net-tools openssh-server sudo zsh git vim

# Configure user
RUN useradd -m johnson && echo "johnson:johnson" | chpasswd && adduser johnson sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN chsh -s `which zsh` johnson

# Copy files
COPY --chown=johnson:johnson cpp/balancer /home/johnson/app/bin/balancer
COPY --chown=johnson:johnson scripts /home/johnson/app/scripts

# configure ssh
RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN mkdir /home/johnson/.ssh
RUN echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDVcYOl/Q/TkpxdA4GYbVda8flEQ3EDTaNoBMzYHQ/owPYXP/vaAT3DL3Lxgs12eslNA9px8wqNckmdUdc0NsUyh8Od1ke2S+FCkC/b2tK75aZ3PQsGJb0z+hdYu1/kFby5WKllTQRgNkvkOhTOWu+ybFeiCrylShMXXrkdC6aBQ8w7qWyaGlr1CBs+cKxAd2zyuYn3E5KiyhJPFZr+hN8EH6Q0wtAwTec8ViosY7pEcdIkBl1RUvwiZdaCv5fnGoax62dzQO7jCTVdBAH3jQifBsMLaLffGKqGjF926DLFwhEpUEKL4B/I3LNehAbV+xDnIkFchucgjNkmXamv5yl7W5PVgdyl3W7SoxKfVut0/0eKUKjRplZrhKVCRNLKqnHA9C3yF8QAYRwhlAOwFarEAi5zJNJV+JniFpNkXCsXdJxuZukHPDVJlY8LVyopxbvjSGTowlwgIoCtJPWbW15nioo0Sm1exVJff50eG6L8oTbFTCIar2YcXz07skqmW1nqE53bEBgqageSsjOcBouS8f7X3xOC66qQB1Oyyi9+gUJF4O6NpLlhFvyJMER3Yl4v89LyqAUi27FGbcn+zzCKELV5zjHTmJ+18EOPYv8h7IIJ4nR31QCD4F1eW1TRt4fXn8oEW/H9H+ItcDKQwSn39ZyK/q1t8hYDV1rzavv59w== johnsonli1993@gmail.com" > /home/johnson/.ssh/authorized_keys
RUN echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDu3PuvoUHJF3vTs+65f+6nfpUwR4dNh9msHkXPGxfnVEK3UPBt2bo4ibwNb15WKFZxSASzvOgagkdCh1grlemhjfPW3pEU40cfzy7j3E4mON2B4t/lA3d2vvTWaM5orDRt3UAsA6UpF479DbmXR6pr6ubUVrtRXoiaMYfF++y7xACvvyCJIj3rRyh78vxS97RuzIOb4YO2K1xdwAwViWNehAidUNZW/QsXyfjhGOZcqqNqDNh8Hrpzl/n1qhaXVPs3o3aXtn9TQS6f5BTET7HtzwjDKjxQOwtWwsYkepJEEj5OkoVk8hcZXZQqWIr1Y3/I4D7bE/1YeDwUSZRU8IL/ johnsonli1993@instance-1" > /home/johnson/.ssh/authorized_keys

USER johnson

RUN wget -q https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

EXPOSE 22
CMD ["/home/johnson/app/scripts/entrypoint.sh"]
