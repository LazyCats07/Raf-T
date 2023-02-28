import pyfiglet #Make it prettier
import sys #used for handling exceptions
import socket #use to basically do all of our port internet
from datetime import datetime #order for our banner to print the date and time on top

ascii_banner = pyfiglet.figlet_format("\nR A F'T")
print(ascii_banner)

target = input(str("Target IP : "))

#Banner 
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning Started at: " + str(datetime.now()))
print("_" * 50)

try:
   #Scan every port on the tarhet ip
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

    #return Open Port
    result = s.connect_ex((target,port))
    if result == 0:
        print("[*] Port {} is open". format(port))
    s.close 

except KeyboardInterrupt:
    print("\n Exiting Program :(")
    sys.exit()

except socket.error:
    print("\ Host Not Responding :( ")
    sys.exit()







