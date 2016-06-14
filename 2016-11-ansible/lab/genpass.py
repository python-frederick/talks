#!/bin/env python

'''
http://docs.ansible.com/ansible/faq.html#how-do-i-generate-crypted-passwords-for-the-user-module
'''

from passlib.hash import sha512_crypt
import getpass

print sha512_crypt.encrypt(getpass.getpass())

