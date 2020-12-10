#!/usr/bin/python36
print("content-type: text/html")
print()


import cgi
import subprocess as sp
mydata=cgi.FieldStorage()  

docname=mydata.getvalue("docname")
img=mydata.getvalue("img")
      


x=sp.getoutput("sudo ansible-playbook --extra-vars 'docname={}' --extra-vars 'img={}' docker.yml".format(docname,img))


