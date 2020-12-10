#!/usr/bin/python36
print("content-type: text/html")
print()


import cgi
import subprocess as sp

mydata=cgi.FieldStorage()

akey=mydata.getvalue("akey")
skey=mydata.getvalue("skey")
bucket=mydata.getvalue("bucket")      


x=sp.getoutput("sudo ansible-playbook --extra-vars 'akey={}' --extra-vars 'skey={}'  --extra-vars 'bucket={}' s3create.yml".format(akey,skey,bucket))

#print(x)
