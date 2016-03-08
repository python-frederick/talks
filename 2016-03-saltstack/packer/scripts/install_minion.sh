#! /bin/bash

# sudo add-apt-repository -y ppa:saltstack/salt
# sudo add-apt-repository -y ppa:saltstack/salt2015-5
wget -O - https://repo.saltstack.com/apt/ubuntu/ubuntu14/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
sudo sh -c 'echo "deb http://repo.saltstack.com/apt/ubuntu/ubuntu14/latest trusty main" >> /etc/apt/sources.list.d/salt.list'

sudo apt-get update
sudo apt-get install -y python-dev python-pip uuid git

sudo apt-get install -y salt-minion
sudo cp /tmp/minion /etc/salt/minion

# clean up downloaded packages
sudo apt-get clean -y

sudo service salt-minion restart
