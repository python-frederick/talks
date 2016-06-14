class: center, middle
![python-frederick](python-frederick.png) ![ansible-logo](ansible_logo.png)
### Python Frederick Aug 2016
### Chris Malone
[surefoot@gmail.com](mail://surefoot@gmail.com) || [github.com/kenfusion](https://github/kenfusion)
???
*DON'T FORGET TO START VAGRANT NOW INSTEAD OF LATER*

---
# Infrastructure as Code?
???
What is it? Let's consult the Book of Knowledge.
--

[en.wikipedia.org/wiki/Infrastructure_as_Code](https://en.wikipedia.org/wiki/Infrastructure_as_Code)
> Infrastructure as Code (IaC) is the process of managing and provisioning computing infrastructure (processes, bare-metal servers, virtual servers, etc.) and their configuration through machine-processable definition files, rather than physical hardware configuration or the use of interactive configuration tools.

???
Infratructure as code is the process of provisioning, configuring and managing all your boxes. It's done with machine readable files, in a repeatable manner.  It's not done mannualy, which is prone to human error.

---
# What tools are available?
???
I'm not going to do a deep dive to each of these tools. I'm just going to name the most popular ones in order by age.
--

## Puppet (2005)
--

## Chef (2009)
--

## SaltStack (2011)
--

## Ansible (2012)

---
# Why Ansible?
???
Instead of describing all of the other tools I'm just going to concentrate on Ansible.  Here's some of the features I like about ansible.
--

### No agents
???
Some tools use agents that live on the nodes that are being managed.  I prefer not to have to deal with installing agents and caring for them as well as the services I'm trying to manage.
--

### No client/server
???
Some tools require a centralized server to manager all the nodes.   With ansible you can manage your nodes from a centralized server or your laptop.  Nodes can also manage themselves as well with simple cron jobs.
--

### Uses established SSH trust
???
Some tools require firewall ports to be opened, certificates to be installed and mantained, forward and backward DNS resolution, in order to communicate between the master server and the agents.  All ansible needs is SSH, which every basic server has.  That's not to say that it's the only way Ansible can communicate, there are others.
--

### Written in python
???
Python.  Nothing wrong with that!

---
# What does Ansible do?
--

* Automation
???
It does automation, which is what everyone wants, right?
--

* Provisioning
???
It does provisioning.
--

* Configuration Management
???
It does configuration management.
--

* Orchestration
???
It does orchestration
--

.center[![Automate](all-the-things.jpg)]
???
It automates all the things!

---
# Automation
???
So let's talk about automation.  Everyone has basic commands they use every day. This is fine for a single server, but what if you want to run the same command on all your servers?
--

### Ad-hoc commands
???
Ansible does this with ease through ad-hoc commands. Ad-hoc commands are simple one-liners you have in your head and don't need to save anywhere. It's a great way to get your feet wet.
--

How long have my nodes been up?
???
What if you want to run the uptime command on all your servers to see how long they all have been up.  You can log in to each server one at a time, and log all the results.  You can get creative and make a script that does it for you, and some of you probably have those.
--

```bash
[vagrant@mgmt ansible]$ ansible all -m shell -a 'uptime' -o
node-03 | SUCCESS | rc=0 | (stdout)  13:11:36 up 4 min,  1 user,  load average: 0.11, 0.04, 0.02
node-04 | SUCCESS | rc=0 | (stdout)  13:11:36 up 3 min,  1 user,  load average: 0.09, 0.05, 0.02
node-01 | SUCCESS | rc=0 | (stdout)  13:11:36 up 5 min,  1 user,  load average: 0.12, 0.06, 0.02
node-02 | SUCCESS | rc=0 | (stdout)  13:11:36 up 4 min,  1 user,  load average: 0.00, 0.00, 0.00
[vagrant@mgmt ansible]$
```
???
This is one way you can do it in ansible.  I just ran a one liner and got the output from each node in a nice report.  I have the nodes, the stdout of the command, even the return code.
--

What OS are all my nodes running?
???
This seems like a simple question to answer. But each OS has a different way of showing this. One common way is to cat out the release files in the etc directory.  Easy enough to do right?  But then you need to parse the output, and something that started out as a simple question becomes a project.
--

```bash
[vagrant@mgmt ansible]$ ansible all -m setup -a 'filter=ansible_os_family' -o
node-01 | SUCCESS => {"ansible_facts": {"ansible_os_family": "RedHat"}, "changed": false}
node-03 | SUCCESS => {"ansible_facts": {"ansible_os_family": "RedHat"}, "changed": false}
node-02 | SUCCESS => {"ansible_facts": {"ansible_os_family": "RedHat"}, "changed": false}
node-04 | SUCCESS => {"ansible_facts": {"ansible_os_family": "RedHat"}, "changed": false}
[vagrant@mgmt ansible]$
```
???
Here's one way of doing it in ansible using the setup module.  I'll talk more about modules later.

---
# Provisioning
--

### Make one type of system into another
???
This is where you take a base system and provision it into a specialized system.
--

Take a base system and provision it into a...
???
You have a system with a fresh OS install, usualy with no packages or services running, and you want to make it into a specialized server.
--

* Web Server

--

* DB Server
--

* Load Balancer

---
# Provisioning

### Basic pattern
???
Here is your basic provisioning pattern that everyone is familiar with.
--

1. Install package
--

2. Edit/Copy configuration files
--

3. Start service
--

4. Enable service
--

5. ...
--

6. Profit!

---
# Configuration Management
--

### Describe the state of your environment
???
This is where you describe the state of your system or environment. It doesn't describe HOW to do it.  It describes the end result.
--

I want a server that has..

???
For example you want a server that's running apache.  You don't care how it gets there. You could be running ubuntu or centos, and that really doesn't matter.
--

* Apache

???
You know you want Apache
--

* Apache version x.x.x

???
You might even want a specific version of Apache.
--

* Apache running
???
You want it to be running.
--

* Apache enabled (survives a reboot)

???
And you definitely want it to survive a reboot.
--

### Enforce it
???
Not only can you describe your environment.  You can enforce it.
--

* Apache disabled => Apache enabled
???
How many times have you forgotten to enable apache after you installed and started it?  You can set up ansible to do all of this for you and make sure the systems that deviate from this are brought back into compliance.

---
# Orchestration
???
I talked either about one system or one type of system so far.  Orchestration comes into play when you want to describe your whole infrastrcuture.
--

### Automate tasks between systems
???
That's usually a mashup of diffrent types of services on different servers.  Here's another basic pattern for configuring a LAMP stack with HA.
--

1. Install NTP on all the servers
--

2. Configure LB Server
--

3. Configure DB Server
--

4. Configure Web Server
--

5. ...
--

6. Profit!

---
name: installing-ansible-linux
# Installing Ansible

[docs.ansible.com/ansible/intro_installation.html](http://docs.ansible.com/ansible/intro_installation.html)
## Linux
???
Installing ansible is pretty straight forward. It's a python module that can be installed with pip or your OS package manager. Currently Ansible can be run from any machine with Python 2.6 or 2.7 installed (Windows isn’t supported for the control machine). See the docs for details.

---
template: installing-ansible-linux
### apt
```bash
sudo apt-get install -y software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible
```

---
template: installing-ansible-linux
### yum
```bash
sudo yum install -y epel-release
sudo yum install -y ansible
```

---
template: installing-ansible-linux
### pip
```bash
pip install ansible
```

---
# Installing Ansible

[docs.ansible.com](http://docs.ansible.com/ansible/intro_installation.html)

## Windows
# :(
???
Unfortunatly managing nodes from Windows is not supported.  That's not to say you can't manage Windows nodes with Ansible.

---
name: inventory
# Inventory
[docs.ansible.com/ansible/intro_inventory.html](http://docs.ansible.com/ansible/intro_inventory.html)

/etc/ansible/host

---
template: inventory
```bash
mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com
```
???
Ansible is uses a INI-like host file.  The default location is /etc/ansible/hosts. You can list servers individually, and you can group them.  You can even have groups of groups. More on that later.

---
template: inventory
```bash
badwolf.example.com:5309
```
???
If you have custom ssh port, you use usual colon to tack on the port number.
--

```bash
jumper ansible_port=5555 ansible_host=192.168.1.50
```
???
You can also make an alias by setting variables.  We'll talk more about variables later.  In this case we're naming a server jumper.  When ansible talks to jumper, it'll do so on that IP and port.
--

```bash
[webservers]
www-[01:50].example.com

[databases]
db-[a:f].example.com
```
???
You can also use ranges.  These will resolve to www-01.example.com through www-50.example.com and db-a.example.com through db-f.example.com

---
template: inventory
```bash
[atlanta]
host1
host2

[raleigh]
host2
host3

[southeast:children]
atlanta
raleigh

[southeast:vars]
some_server=foo.southeast.example.com
halon_system_timeout=30
self_destruct_countdown=60
escape_pods=2
```

???
You can make groups of groups using the :children suffix. You can assign variables to groups using the :vars suffix. I would advise against using the host files to store your variables.  There's a better place to do that, which I'll show later.

---
# Dynamic Inventory
[docs.ansible.com/ansible/intro_dynamic_inventory.html](http://docs.ansible.com/ansible/intro_dynamic_inventory.html)

.center[![dynamic](dynamic.jpg)]
???
If you have a lot of hosts that change, such as in a cloud envrionment, or you want to maintain your inventory in a separate system, ansible supports that as well.  Read more about dynamic inventory in the documentation.

---
# Playbooks
```yaml
---
- hosts: webservers
  vars:
    http_port: 80
    max_clients: 200
  remote_user: root
  tasks:
  - name: ensure apache is at the latest version
    yum: name=httpd state=latest
  - name: write the apache config file
    template: src=/srv/httpd.j2 dest=/etc/httpd.conf
    notify:
    - restart apache
  - name: ensure apache is running (and enable it at boot)
    service: name=httpd state=started enabled=yes
  handlers:
    - name: restart apache
      service: name=httpd state=restarted
```
???
Playbooks are written in YAML format.  YAML is a nice format for humans to read and machines can parse it as well.  The best part about YAML is, unlike JSON, you can comment it. A playbook is a list of plays. It can be a single play or as many as you like. This is a single play.  It follows the pattern I mentioned earlier.  It installs apache, conigures it, restarts it and even enables it.

---

# Playbooks
```yaml
---
- hosts: webservers
  vars:
    http_port: 80
    max_clients: 200
  remote_user: root
  tasks:
  - name: ensure apache is at the latest version
    yum:
      name: httpd
      state: latest
  - name: write the apache config file
    template:
      src: /srv/httpd.j2
      dest: /etc/httpd.conf
    notify:
    - restart apache
  - name: ensure apache is running
    service:
      name: httpd
      state: started
  handlers:
    - name: restart apache
      service:
        name: httpd
        state: restarted
```
???
This is the exact same play but written in a slightly different format. It uses YAML dictionary types to provide arguments.  I prefer this way of writing play books.  It results more lines, but it's more clean, IMO.

---
# Variables

[docs.ansible.com/ansible/playbooks_variables.html](http://docs.ansible.com/ansible/playbooks_variables.html)

```yaml
- hosts: webservers
  vars:
    src: /srv/myfiles/foo.conf
    dest: /etc/foo.conf
```
???
I mentioned variables before and how they can be stored in your inventory file, but you can also put them in a play.  You can also put them in a seperate file and include them.
--

```yaml
  tasks:
  - name: copy host file
    copy:
      src: "{{ src }}"
      dest: "{{ dest }}"
      owner: foo
      group: foo
      mode: 0644
```
???
When referencing them in a playbook you use double curly braces.  Since playbooks are in yaml, you need to surround these references in quotes.  You don't need to worry about that in templates.

---
# Modules

```yaml
  - name: ensure apache is at the latest version
    yum:
      name: httpd
      state: latest
```
???
Modules are the work horses of ansible. Each task in a play runs a module.  Here is the yum module.
--

```yaml
  - name: write the apache config file
    template:
      src: /srv/httpd.j2
      dest: /etc/httpd.conf
    notify:
    - restart apache
```
???
Here is the template module. Notice the notify directive. This is for a special task called handlers. Which I'll talk about later.
--

```yaml
  - name: ensure apache is running
    service:
      name: httpd
      state: started
```
???
And here is the service module.
--

```bash
ansible-doc yum
```
???
There is also a *man* command to look at module documentation called ansible-doc.  Run that with a name of a module to get that module's documentation.  You can also get documentation online.
--

```bash
ansible-doc -l
```
???
Run ansible-doc -l to get a list.
--

[docs.ansible.com/ansible/modules_by_category.html](http://docs.ansible.com/ansible/modules_by_category.html)
???
There is also module index on the ansible site where you can read all about the modules included with ansible.

---
# Handlers
```yaml
  - name: write the apache config file
    template:
      src: /srv/httpd.j2
      dest: /etc/httpd.conf
    notify:
    - restart apache
```
???
As mentioned before you can use a notify directive in tasks.  This notfies another special task called handlers.
--

```yaml
  handlers:
    - name: restart apache
      service:
        name: httpd
        state: restarted
```
???
These handlers will only run if they get a notify during the play. They will also only run once, and at the end of the play, even if multiple notifications are recieved. Here the handler restarts apache.  It's only run if this configuration file task is ran.

---
class: center,middle
![demo](demo.jpg)
???
And now for the demo!

---
class: center,middle
![environment](environment.jpg)
???
But before we get started I want to describe the lab environment.

---
# /etc/hosts

```bash
10.0.15.21  node-01
10.0.15.22  node-02
10.0.15.23  node-03
10.0.15.24  node-04
10.0.15.25  node-05
10.0.15.26  node-06
```
???
I added 6 nodes to the /etc/hosts files on the management node.

---
# .ansible.cfg

```bash
[defaults]
inventory = $HOME/ansible/inventory
host_key_checking = False
gathering = smart
fact_caching = jsonfile
fact_caching_connection = /vagrant/fact_caching
fact_caching_timeout = 86400
forks = 10
```
???
The .ansible.cfg in your home directory is one place you can configure ansible from.  Here I'm overiding a few settings. There is a custom location for the inventory file.  Host Key Checking is off.  Forks is 10 (default is 5 and you can set this pretty high).  The rest I'll talk about later if there's time.

---
# $HOME/ansible/inventory

```bash
[lb]
node-01

[db]
node-02

[web]
node-03
node-04
#node-05
#node-06

```
???
Here I have the 6 nodes in different groups. 2 are commented out. (You can do that in inventory files).  I'll spin them up later in the demo.

---
class: center,middle
![enough](enough.jpg)

---
# Advanced topics
* Template (jinja2)
* Roles
* Vault
* Ansible Galaxy
* Tower

# Bonus topic
* Cowsay
---
class: center, middle
# Questions?
---

# Software used
* Lab envrionment: [Vagrant](https://www.vagrantup.com/)
* Presentation Software: [Remark.js](http://remarkjs.com/#1)
* Gitub: [python-frederick/talks](https://github.com/python-frederick/talks)
