import getpass
import telnetlib

user = input("Enter your remote account: ")
password = getpass.getpass()
# specifies range of host ip addresses
for x in range (232,236):
    HOST = "192.168.122." + str(x)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        tn.write(b"enable\n")
        tn.write(b"cisco\n")
        tn.write(b"conf t\n")

        for n in range (2,50):
            tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
            tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")


            tn.write(b"end\n")
            tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
