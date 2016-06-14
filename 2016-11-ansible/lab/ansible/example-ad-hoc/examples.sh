#!/bin/env bash

# ansible all -m ping

# ansible all -m setup

# ansible all -a 'uptime'

# ansible all -m yum -a "name=ntp state=installed"

# ansible all -m yum -a "name=ntp state=installed" -b

# ansible all -m yum -a "name=ntp state=absent" -b
