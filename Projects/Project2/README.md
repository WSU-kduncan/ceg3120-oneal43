- Name: Michael O'Neal
- Email: oneal.43@wright.edu
- Project 2

## Part 1

1. VPC created & configured & role described
   ![vpc](Images/ONeal-VPC.png)
  - VPC known as Virtual Private Cloud enables users to launch AWS resources into a virtual network that resembles a traditional network.
2. Subnet created & configured & role described
   ![subnet](Images/ONeal-Subnet.png)
  - A subnet is a range of IP adresses in the VPC that you can launch AWS resources into. This includes both public and private subnets that can be used for a variety of reasons. 
3. Internet gateway created & configured & role described
   ![gateway](Images/ONeal-gw.png)
  - An internet gateway enables resources in your public subnets (such as EC2 instances) to connect to the internet if the resource has a public IPv4 address or an IPv6 address. 
4. Route table created and configured & role described
   ![routetable](Images/ONeal-routetable.png)
   ![routetable rule](Images/routes.png)
  - A route table contains a set of rules, called routes, that determine where network traffic from your subnet or gateway is directed.
5. Security group created and configured & role described
   ![Security Groups](Images/SGs.png)
   - A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.

## Part 2`

1. Instance details
   - AMI selected
	```Ubuntu```
   - default username of the instance type selected
	```ami-08c40ec9ead489470```
   - Instance type selected
	```t2.micro```
2. How to attach instance to VPC
  - The instance is connected to the VPC via the subnet. To do this, ensure that when creating the subnet, you are assigning valid CIDR blocks that correspond with the range associated with the VPC. 
3. Public IP address auto-assign - yay or nay and why?
  - Nay. I do not want me instance to be publicly available and I have also assigned an EIP address to the instance therefore, I do not need to auto-assign a public IP address.
4. How to create and attach storage volume to instance
  - Under configure storage, there are two different methods to adding storage volumes to your instance. I opted to use simple but there is the option to use advanced where you can dictate size, volume type, add encryption, and choose if the volume is deleted when the instance is terminated. 
5. How to tag instance with "Name" of "YOURLASTNAME-instance"
  - When creating an instance, you have the abiity to tag the instane and give it a name. 
6. How to associate VPC security group (your security group) with your instance
  - To associate VPC security groups with my instance, under "Firewall (security groups)" in the instance, check "Select existing security group". You can then see all security groups for the instance under "Common security groups". Select the security group for the VPC that was created in an earlier step.
7. How to create / reserve and associate and Elastic IP address with your instance
  - Navigate to Elastic IPs
  - Click Allocate Elastic IP address
  - Ensure us-east-1 is selected
  - Ensure Amazon's pool of IPv4 addresses is selected
  - Add a new tag with the key "Name" and Value "ONeal-EIP"
  - Click allocate
  - Select ONeal-EIP
  - Click on Actions
  - Click Associate Elastic IP address
  - Choose INstance for Resource type
  - Choose the instance created for this project ONeal-Instance
  - Select IP address that is populated when you click on the text box for Private IP Address.
  - Click Associate
8. Screenshot with instance details
   ![Instance details](Images/instance-details.png)
9. How to change hostname via commands on instance
  - sudo hostnamectl set-hostname ONeal-Ubuntu
  - Created copy of /etc/hosts named /etc/hosts-old
  - Edited /etc/hosts by replacing local host with ONeal-Ubuntu
  - Disconnected ssh
  - Reconnected via ssh to reflect changes
10. Screenshot of successful SSH connection to instance (with your new hostname instead of ip-##-##-##-##)
   ![ssh connection](Images/ssh-connection.png)
