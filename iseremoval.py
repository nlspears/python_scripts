##imports python modules needed to work
from netmiko import ConnectHandler
import time, sys, getpass, paramiko

user = raw_input("Enter your SSH username: ")
pword = getpass.getpass()

device = {
    'device_type': 'cisco_ios',
    #'ip': '192.168.43.10',
    'username': user,
    'password': pword,
    #'secret':'password'
}
net_connect = ConnectHandler(**device)
ipfile=open("iplist.txt") #This file contains a list of switch ip addresses.

for line in ipfile:
    device['ip']=line.strip()
    print("Connecting to Device " + line)
    net_connect = ConnectHandler(**device)
    time.sleep(2)
    print ("Checking Interface Configurations")
    intfilter = net_connect.send_command("sh run | i Gi.")
    striplist = intfilter.strip()
    intfaces = striplist.splitlines()
    for x in intfaces:
       intconfig = net_connect.send_command("sh run " + x + " | i dot1x")
       findise = intconfig.find("dot1x")
       if findise > 0:
           isefile=open("isefile.txt") #opening the config file with the changes you want to push
           iseconfig=isefile.read() ##reads the config file
           isefile.close() #closes the config file
           commands = [x, iseconfig]
           print ("Applying Configuration to " + x)
           gigintconfig = net_connect.send_config_set(commands)
           print(gigintconfig)
       else:
           print("Non-ISE interface")
           
