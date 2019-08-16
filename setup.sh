#!/bin/sh
#get update
echo "update"
sudo apt -y update
sudo apt -y dist-upgrade
echo "update done"

# install modules
echo "starting install"
echo "install with apt"
sudo apt -y install rpi-update
sudo apt -y install python3-pip
sudo apt -y install git
sudo apt -y install python-dev
sudo apt -y install exfat-fuse exfat-utils
echo "apt install done"
#install python modules
echo "start install with pip"
yes | sudo pip3 install -U pip
yes | sudo pip3 install setuptools
yes | sudo pip3 install -r ./sensorSystem/update/requirements.txt
sudo apt -y install python3-pandas
echo "install phase had done successfully"

#set up C3lessSensorSystem
sudo chmod -R +x /home/pi/C3lessSensorSystem

#get RootCA
echo "getting rootCA for AWS"
wget https://www.amazontrust.com/repository/AmazonRootCA1.pem -P /home/pi/C3lessSensorSystem/sensorSystem/certs

#register systems
echo "register as system" 
sudo mv /home/pi/C3lessSensorSystem/sensorSystem/configs/startPython.service /etc/systemd/system/startPython.service
sudo systemctl enable startPython
sudo systemctl start startPython

echo "set parmission as 755"
chmod 755 ~/C3lessSensorSystem

echo "system done"
echo "setup had done successfully"
