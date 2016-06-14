#!/bin/bash

set -e

#install insecure vagrant key

wget -q https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant -O /home/vagrant/.ssh/id_rsa
chmod 600 /home/vagrant/.ssh/id_rsa

#install ansible

## rhel, centos http://docs.ansible.com/ansible/intro_installation.html#latest-release-via-yum
sudo yum install -y epel-release
sudo yum install -y ansible

## ubuntu/trusty64 http://docs.ansible.com/ansible/intro_installation.html#latest-releases-via-apt-ubuntu
# sudo apt-get install -y software-properties-common
# sudo apt-add-repository ppa:ansible/ansible
# sudo apt-get update
# sudo apt-get install -y ansible

# update /etc/hosts
sudo bash -c  "cat << EOF >> /etc/hosts
10.0.15.10  mgmt
10.0.15.21  node-01
10.0.15.22  node-02
10.0.15.23  node-03
10.0.15.24  node-04
10.0.15.25  node-05
10.0.15.26  node-06
EOF"

# install decom script
mkdir -p $HOME/bin && ln -s /vagrant/decom.sh $HOME/bin/decom

#test ansible local
printf "\nTesting ansible installation\n"
ansible all -i 'localhost,' -c local -m ping
printf "\nIf you see this message, bootstrap script didn't bomb out.  Good job!\n"
