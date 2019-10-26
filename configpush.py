##imports python modules needed to work
from netmiko import ConnectHandler
import time, sys, getpass, paramiko
#import json
#from napalm import get_network_driver

##selects the correct Netmiko class based upon the device_type.
## I then define a network device dictionary consisting of a device_type, ip, username, and password.
device = {
    'device_type': 'cisco_ios',
    #'ip': '192.168.43.10',
    'username': 'cisco',
    'password': 'cisco',
    #'secret':'password'
}
ipfile=open("iplist.txt") #This file contains a list of switch ip addresses.
#print ("Please doublecheck your configuration in the config file. Please stop and figure out what you're about to do...")
#device['username']=input("Enter your SSH username:  ")
#device['password']=getpass.getpass()
configfile=open("configfile.txt") #opening the config file with the changes you want to push
configset=configfile.read() ##reads the config file
configfile.close() #closes the config file

for line in ipfile:
    device['ip']=line.strip()
    print("Connecting to Device " + line)
    #driver = get_network_driver('ios')
    #switches = driver(line,'cisco', 'cisco')
    net_connect = ConnectHandler(**device)
    #net_connect.enable()
    #switches.open()
    time.sleep(2)
    print ("Applying Configuration to Device " + line)
    output = net_connect.send_config_set(configset)
    print(output)
