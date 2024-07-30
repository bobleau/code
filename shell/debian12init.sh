#!/bin/sh

timedatectl set-timezone Asia/Shanghai
echo sleep-inactive-ac-timeout=0 >> /etc/gdm3/greeter.dconf-defaults
apt-mark manual desktop-base network-manager-gnome gnome-terminal file-roller
apt purge -y ace-of-penguins aisleriot atomix cheese evolution five-or-more four-in-a-row gbrainy gnome-2048 gnome-calendar gnome-characters gnome-chess gnome-clocks gnome-contacts gnome-klotski gnome-mahjongg gnome-maps gnome-mines gnome-nibbles gnome-robots gnome-sound-recorder gnome-sudoku gnome-sushi gnome-taquin gnome-tetravex gnome-todo gnome-weather hitori iagno libreoffice* lightsoff quadrapassel rhythmbox simple-scan swell-foop tali transmission-gtk yelp
cat < /etc/apt/sources.list
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bookworm-security main contrib non-free non-free-firmware
EOF
apt update && apt upgrade && sudo apt install -y isenkram-cli && isenkram-autoinstall-firmware
apt install -y smartmontools sshpass rsync iperf3 ethtool inxi stress stress-ng ipmitool sudo xrdp
usermod --append --group sudo nrduser1
apt clean
apt autoremove
apt purge '~c'
apt purge '~o'