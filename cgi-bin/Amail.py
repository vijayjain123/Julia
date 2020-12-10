#!/usr/bin/python36

import cgi
import subprocess as sp
print("content-type: text/html")
print()

form=cgi.FieldStorage()
username=form.getvalue('username')

password=form.getvalue('password')
recipient=form.getvalue('recipient')
subject=form.getvalue('subject')

x=sp.getoutput("sudo ansible-playbook --extra-vars 'username={}' --extra-vars 'password={}' --extra-vars 'recipient={}' --extra-vars 'subject={}'  mail4.yml".format(username, password, recipient, subject )) 

print(x)

