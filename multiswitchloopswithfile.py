import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open ('myswitches') #refer to file call myswitches

for IP in f:
    IP = IP.strip() #strips whitespace before or after each entry in myswitches file
    print ("Configuring Switch " + (IP))
    HOST = IP  #HOST variable replaced with IP address in file myswitches
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")
    for n in range (51,101):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
