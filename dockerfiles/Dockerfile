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

USER johnson

RUN wget -q https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

EXPOSE 22
CMD ["/home/johnson/app/scripts/entrypoint.sh"]
