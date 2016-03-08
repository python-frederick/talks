#! /bin/bash

sudo cp /tmp/setup_server.sh /usr/local/bin/setup_server.sh
sudo chmod +x /usr/local/bin/setup_server.sh

wget -O - https://repo.saltstack.com/apt/ubuntu/ubuntu14/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
sudo sh -c 'echo "deb http://repo.saltstack.com/apt/ubuntu/ubuntu14/latest trusty main" >> /etc/apt/sources.list.d/salt.list'
sudo apt-get update
sudo apt-get install -y python-dev python-pip git

sudo apt-get install -y salt-master
sudo cp /tmp/master /etc/salt/master

# clean up downloaded packages
sudo apt-get clean -y

sudo service salt-master restart
