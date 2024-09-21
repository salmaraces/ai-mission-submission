docker run -it -v "%cd%/src:/home/user" debug_image
docker run -it -v "%cd%/src:/home/user" debug_image
ls -l /home/user
exit
ls -l /home/user
cmake .
make
FROM ubuntu:jammy
# Install dependencies
RUN apt-get update &&     apt-get install -y software-properties-common build-essential wget
# Install a specific version of CMake (e.g., 3.25.0)
RUN wget https://github.com/Kitware/CMake/releases/download/v3.25.0/cmake-3.25.0-Linux-x86_64.sh &&     chmod +x cmake-3.25.0-Linux-x86_64.sh &&     ./cmake-3.25.0-Linux-x86_64.sh --skip-license --prefix=/usr/local
# Create User
ENV USER_NAME=user
RUN useradd -ms /bin/bash $USER_NAME
RUN echo "$USER_NAME:$USER_NAME" | chpasswd && adduser $USER_NAME sudo
RUN echo "$USER_NAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER $USER_NAME
# Set working directory
WORKDIR /home/$USER_NAME
docker build -t debug_image .
exit
docker run -it -v "%cd%/src:/home/user" debug_image
exit
