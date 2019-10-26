##imports python modules needed to work
from netmiko import ConnectHandler
import time, sys, getpass, paramiko
#import json
#from napalm import get_network_driver

##selects the correct Netmiko class based upon the device_type.
## I then define a network device dictionary consisting of a device_type, ip, username, and password.

user = raw_input("Enter your SSH username: ")
pword = getpass.getpass()


device = {
    'device_type': 'cisco_ios',
    #'ip': '192.168.43.10',
    'username': user,
    'password': pword,
    #'secret':'password'
}
ipfile=open("iplist.txt") #This file contains a list of switch ip addresses.

command = "copy run start"

for line in ipfile:
    device['ip']=line.strip()
    print("Connecting to Device " + line)
    net_connect = ConnectHandler(**device)
    #net_connect.enable()
    #switches.open()
    time.sleep(2)
    print ("Applying Configuration to Device " + line)
    print(net_connect.find_prompt())
    output = net_connect.send_command(command)
    net_connect.disconnect()
    print(output)
