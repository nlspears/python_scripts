import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open ('myswitches') #refer to file call myswitches

for IP in f:
    IP = IP.strip() #strips whitespace before or after each entry in myswitches file
    print ("Getting Running Configuration from Switch " + (IP))
    HOST = IP  #HOST variable replaced with IP address in file myswitches
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switch_" + HOST, "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close
