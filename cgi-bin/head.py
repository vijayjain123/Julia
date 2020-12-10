#!/usr/bin/python36

import cgi
import subprocess as sp
print("content-type: text/html")
print()

form=cgi.FieldStorage()
data=form.getvalue('q')


if 'mail' in data and 'send' in data:
    print('<a href="http://192.168.43.161/mail.html">"Mail"</a>')


if 'start' in data and 'docker' in data:
    print('<a href="http://192.168.43.161/docker.html">"Docker"</a>')

if 'add' in data and 'user' in data:
    print('<a href="http://192.168.43.161/useradd.html">"User window will be opened"</a>')
if 'start' in data and 'ec2' in data:
    print('<a href="http://192.168.43.161/ec2.html">"ec2"</a>')
if 'create' in data and 'ebs' in data:
    print('<a href="http://192.168.43.161/ebs.html">"ebs"</a>')
if 'create' in data and 's3' in data:
    print('<a href="http://192.168.43.161/s3.html">"s3"</a>')
if 'hadoop' in data and 'cluster' in data:
    print('<a href="http://192.168.43.161/hadoop.html">"Hadoop cluster"</a>')
if 'container' in data and 'service' in data:
    print('<a href="http://192.168.43.161/caas1.html">"CAAS"</a>')

