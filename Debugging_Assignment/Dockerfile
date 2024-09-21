FROM ubuntu:jammy

RUN apt-get update && \
    apt-get install -y software-properties-common sudo wget gcc build-essential

RUN wget https://github.com/Kitware/CMake/releases/download/v3.25.0/cmake-3.25.0-linux-x86_64.sh -O /tmp/cmake-install.sh && \
    chmod +x /tmp/cmake-install.sh && \
    /tmp/cmake-install.sh --skip-license --prefix=/usr/local && \
    rm /tmp/cmake-install.sh

ENV USER_NAME=user

RUN useradd -ms /bin/bash $USER_NAME && \
    echo "$USER_NAME:$USER_NAME" | chpasswd && adduser $USER_NAME sudo && \
    echo "$USER_NAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER $USER_NAME

WORKDIR /home/$USER_NAME

RUN mkdir -p /home/$USER_NAME/build
