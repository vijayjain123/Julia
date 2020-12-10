#!/usr/bin/python36
print("content-type: text/html")
print()



print("""
        <table border='5'>
        <tr>
        <td>Container_name</td>
        <td>Container_image</td>
        <td>Status</td>
        </tr>
        </table>
""")
import subprocess

x="sudo docker ps -a"

output=subprocess.getoutput(x)
container_list=output.split("\n")
print(output)

'''
for c in container_list[1:]:
   if 'Up' in c:
       cstatus="running"
   elif "Exited" in c:
       cstatus="stopped"
   else:
       cstatus="unknown staus"
       
   c_details=c.split()  
  cname=c_details[-1]
   imgname=c_details[1]
   print( 
   <tr>
   <td>{}</td>
   <td>{}</td>
   <td>{}</td>
   </tr>
   .format(cname,imgname,cstatus)))
print("</table>")
'''
