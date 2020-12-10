#!/usr/bin/python36
print("content-type: text/html")
print()

import subprocess as ap
print(ap.getoutput("ansible-playbook useradd.yml"))
