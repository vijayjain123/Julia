#!/usr/bin/python36
print("content-type: text/html")
print()

import cgi
import subprocess as sp
mydata=cgi.FieldStorage()  

akey=mydata.getvalue("akey")
skey=mydata.getvalue("skey")
vol=mydata.getvalue("vol")


x=sp.getoutput("sudo ansible-playbook --extra-vars 'akey={}' --extra-vars 'skey={}' --extra-vars 'vol={}' ebsvolume.yml".format(akey,skey,vol))

#print(x)
