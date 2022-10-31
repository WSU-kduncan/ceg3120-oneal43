Name: Michael ONeal
Email: oneal.43@wright.edu
Project 4

## Part 2 - Setup Load Balancing TODOs

**Using the instances created by your CloudFormation template, setup the following and add documentation or screenshots to your `README.md` file as specified.**

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs of systems within the subnet (your instances).
   - Description of how file is configured
```
I setup a config file for webserv1, webserv2, and proxy. The config file contains the private ip addresses for each server, the user, and the path to the private key which allows an ssh connection. 
```
2. Document how to SSH in between the systems utilizing their private IPs.
```
To ssh between each instance utilizing their private IPs, I created config on each instance so that I could simply typ ssh "server name" to switch between each one.
```
3. **_HAProxy configuration & documentation requirements_**
   - How to set up a HAProxy load balancer
```
Both frontend and backend were used in the configurations for haproxy. The frontend used the private ip for the proxy to listen on port 80 before pointing to the backend webservers. The backend webservers listened on port 80 on both webserv1 and webserv2's private ip addresses. 
```
   - What file(s) where modified & their location
```
/etc/haproxy/haproxy.cfg
```
     - What configuration(s) were set (if any)
```
* global
  * maxconn was set from 5000 to 1000
  * all default ssl material locations were commented out

* defaults
  * timeout connect chnaged from 5000 to 10s
  * timeout clinet was changed from 50000 to 30s
  * timeout server was changed from 50000 to 30s

*Added the below configurations for backend and frontend web servers

* frontend web_servers
  * bind 10.0.0.10:80
  * default_backend web_servers

* backend web_servers
  * balance roundrobin
  * option httpchk HEAD /
  * server webserv1 10.0.1.10:80
  * server webserv2 10.0.1.20:80

```
     - How to restart the service after a configuration change
```
systemctl restart haproxy.service
systemctl reload haproxy
```
     - Resources used (websites)
4. **_Webserver 1 & 2 configuration & documentation requirements_**
   - How set up a webserver
     - What file(s) were modified & their location
```
TO set up the webserver, index.html located at /var/www/html was modified to reflect onctent on both webservers.
```
     - What configuration(s) were set (if any)
```
Nothing additional was configured for apache2.
```
     - Where site content files were located (and why)
```
The site content files are located in /var/www/html. THis is the location for the original apache2 site content so it was replaced with the content for this project.
```
     - How to restart the service after a configuration change
```
sudo service apache2 restart
```   
     - Resources used (websites)
5. From the browser, when connecting to the proxy server, take two screenshots.
   - one screenshot that shows content from "server 1"
   - one screenshot that shows content from "server 2"
6. (Optional) - link to your proxy so I can click it.
