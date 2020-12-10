#!/usr/bin/python36
print("content-type: text/html")
print()


import cgi
import subprocess as sp

mydata=cgi.FieldStorage()
user=mydata.getvalue("user")
upass=mydata.getvalue("upass")
x=sp.getoutput("sudo ansible-playbook --extra-vars 'user={}' --extra-vars 'upass={}' useradd.yml ".format(user,upass))
#print(x)

