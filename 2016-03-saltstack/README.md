# Setup virtualbox
Virtualbox does all of the virtualization of the instances.

https://www.virtualbox.org/wiki/Downloads

# Setup vagrant
Vagrant abstracts the management of the virtualboxs away from the users into the vagrant file.

https://www.vagrantup.com/docs/installation/

# Setup packer
Packer sets up the instances salt and salt-minion with the prebuilt install scripts.

https://www.packer.io/intro/getting-started/setup.html

## Install landrush
Landrush (when it works) sets up local dns resolution of the salt/salt-minion.domain.develop instances.

The packer *null* build relies on the landrush plugin for dns.
```
vagrant plugin install landrush
```

# Build instances
```
cd ~/git/python-frederick-salt-talk
vagrant up --provider virtualbox
vagrant landrush list
```
update /etc/hosts if needed, on some linux boxes landrush does not work.
```
cd packer
packer.io build -only null ./server.json
packer.io build -only null ./minion.json
```
# Login and demo prep
Master
```
vagrant ssh salt
sudo -s
cd /srv
```
Minion
```
vagrant ssh salt-minion
sudo -s
tail -f /var/log/salt/minion
```

# Run salt commands

```
salt '*' test.ping
salt 'salt-minion*' grains.items
salt 'salt-minion*' grains.item id
```

# View nginx state
```
vim salt/nginx/init.sls
vim salt/nginx/server.sls
vim salt/top.sls
```
add - nginx to salt-minion.domain.develop

```
salt 'salt-minion*' state.highstate
```

Go to http://salt-minion

```
vim salt/nginx/test.txt
```
Add text to the test file

```
vim salt/nginx/init.sls
```
Add the following:
```
/usr/share/nginx/html/test.txt:
  file.managed:
    - source: salt://nginx/test.txt
```
Run:
```
salt 'salt-minion*' state.highstate
----------
     ID: /usr/share/nginx/html/test.txt
Function: file.managed
 Result: True
Comment: File /usr/share/nginx/html/test.txt updated
Started: 21:29:30.136948
Duration: 16.621 ms
Changes:
         ----------
         diff:
             New file
         mode:
             0644
---------
```

## On minion
Run:
```
cat /usr/share/nginx/html/test.txt
```
Go to http://salt-minion/test.txt
