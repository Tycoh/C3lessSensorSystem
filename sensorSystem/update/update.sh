#!/bin/sh
sudo apt -y update
sudo apt -y upgrade
sudo dpkg --configure -a
sudo apt -y dist-upgrade
sudo pip3 install -U pip
sudo pip3 install -U -r /home/pi/C3lessSensorSystem/sensorSystem/update/requirements.txt
sudo apt -y clean
sudo apt -y autoremove
