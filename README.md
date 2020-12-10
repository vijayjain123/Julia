# Julia
Julia is an advance virtual assitance tool for developers. It aims at developing a market ready web service for RedHat which can provide a number of services in a safe and secure way.

# Services
* Cloud services
    * SAAS
    * CAAS
    * IAAS
* AWS
    * Ec2
    * EBS
    * S3
* Through this web app user can operate linux terminal from anywhere
* Automation of hadoop HDFS cluster using Ansible

# Setup
* Operating system - RedHat
* Download the code and save it in /var/www/
* Open terminal >> ifconfig 
* Check your ipaddress
* Change ipaddress in all files to that of your laptop ipaddress
* Run the following commands in the terminal -
   * systemctl restart httpd
   * systemctl enable httpd
   * iptables -F 
   * setenforce 0
