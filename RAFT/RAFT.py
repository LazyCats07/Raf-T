# Import Library
# !/usr/bin/env python
import socket    # Digunakan untuk berkomunikasi dengan mesin lain menggunakan protokol TCP dan UDP 
import platform
import termcolor # Mencetak beberapa pernyataan dalam warna yang berbeda 
import os
# Import scapy
import scapy.all as scapy
# We need to create regular expressions to ensure that the input is correctly formatted.
import re
import time

os.system("cls")

#Basic Interface
print(r"""
    ██████╗░  ░█████╗░  ███████╗  ██╗  ████████╗
    ██╔══██╗  ██╔══██╗  ██╔════╝  ╚█║  ╚══██╔══╝
    ██████╔╝  ███████║  █████╗░░  ░╚╝  ░░░██║░░░
    ██╔══██╗  ██╔══██║  ██╔══╝░░  ░░░  ░░░██║░░░
    ██║░░██║  ██║░░██║  ██║░░░░░  ░░░  ░░░██║░░░
    ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═╝░░░░░  ░░░  ░░░╚═╝░░░""")
print("\n****************************************************************")
print("\n* My Scanner Tool                                              *")
print("\n****************************************************************")
respon = input("""\n Please enter the type of scan you want to run
                1. Port Scanner
                2. OS Scanner
                3. Network Scanner 
Input: """)
print("You have selected option: ", respon)

# ----------------------------------------------------------------------------------------------------------
if respon == '1':
    os.system("cls")
    #Basic Interface
    print(r"""
        ██████╗░  ░█████╗░  ███████╗  ██╗  ████████╗
        ██╔══██╗  ██╔══██╗  ██╔════╝  ╚█║  ╚══██╔══╝
        ██████╔╝  ███████║  █████╗░░  ░╚╝  ░░░██║░░░
        ██╔══██╗  ██╔══██║  ██╔══╝░░  ░░░  ░░░██║░░░
        ██║░░██║  ██║░░██║  ██║░░░░░  ░░░  ░░░██║░░░
        ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═╝░░░░░  ░░░  ░░░╚═╝░░░""")
    print("\n****************************************************************")
    print("\n* Port Scanner Tool                                            *")
    print("\n****************************************************************")

    # Process
    def scan(targets, ports):
        print('\n' + ' Starting Scan For ' + str(targets))
        for port in range(1,ports): # Akan melakukan pengulangan dari jumlah inputan yang di isi 
            scan_port(targets, port)

    def scan_port(ipaddress, port):
        try : 
            # try to menginisasi objek socket  
            sock = socket.socket()
            # terhubung ke port tertentu pada alamat IP tertentu yang akan ditentukan nanti. 
            sock.connect((ipaddress, port)) 
            # Menampilkan atau print hasil dari fungsi di atas 
            print(termcolor.colored( ("\t[+] Port Terbuka " + str(port)),'green'))
            # Setelah berhasil menyelesaikan suatu tindakan, seperti menemukan port terbuka, Kita bisa menutup objek socket
            sock.close()
        except : # Jika tidak berhasil terhubung, maka itu akan melanjutkan ke pernyataan "Except" yang akan melakukan print  "Port Tertutup"
                # print("[-] Port Closed " + str(port))
                pass

    # Bagian Input 
    # Input Target IP
    print("Ex : 192.168.1.1-192.168.1.5")	 
    targets = input(termcolor.colored(("[*] Enter Targets to Scan (Split them by - ): "),'blue'))
    # input Jumlah target port
    ports = int(input(termcolor.colored(("[*] Enter How Many Ports You Want to Scan: "),"blue")))

    if '-' in targets:
        print(termcolor.colored(("[*]Scanning Multiple Targets"), 'yellow'))
        for ip_addr in targets.split('-'):
            scan(ip_addr.strip(' '), ports)
    else:
        scan(targets,ports)

# --------------------------------------------------------------------------------------
elif respon == '2':
    os.system("cls")

    def get_os_info():
        os_name = platform.system()
        os_version = platform.release()
        return os_name, os_version

    def get_net_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(r"""
        ██████╗░  ░█████╗░  ███████╗  ██╗  ████████╗
        ██╔══██╗  ██╔══██╗  ██╔════╝  ╚█║  ╚══██╔══╝
        ██████╔╝  ███████║  █████╗░░  ░╚╝  ░░░██║░░░
        ██╔══██╗  ██╔══██║  ██╔══╝░░  ░░░  ░░░██║░░░
        ██║░░██║  ██║░░██║  ██║░░░░░  ░░░  ░░░██║░░░
        ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═╝░░░░░  ░░░  ░░░╚═╝░░░""")
        print("\n****************************************************************")
        print("\n* OS Scanner Tools                                             *")
        print("\n****************************************************************\n")
        net_ip = input(termcolor.colored(("Input The IP : "), "blue"))
        s.connect((net_ip, 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address

    if __name__ == "__main__":
        os_name, os_version = get_os_info()
        ip_address = get_net_ip()
        
        os.system('cls')
        print(f"\nOperating System\t: {os_name} {os_version}")
        print(f"Local IP Address\t: {ip_address} \n")

# ------------------------------------------------------------------------------------
elif respon == '3':
    os.system("cls")


    # Basic user interface header
    print(r"""
    ██████╗░  ░█████╗░  ███████╗  ██╗  ████████╗
    ██╔══██╗  ██╔══██╗  ██╔════╝  ╚█║  ╚══██╔══╝
    ██████╔╝  ███████║  █████╗░░  ░╚╝  ░░░██║░░░
    ██╔══██╗  ██╔══██║  ██╔══╝░░  ░░░  ░░░██║░░░
    ██║░░██║  ██║░░██║  ██║░░░░░  ░░░  ░░░██║░░░
    ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═╝░░░░░  ░░░  ░░░╚═╝░░░""")
    print("\n****************************************************************")
    print("\n* Network Scanning Tools                                       *")
    print("\n****************************************************************")

    # Regular Expression Pattern to recognise IPv4 addresses.
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

    # Get the address range to ARP
    while True:
        ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
        if ip_add_range_pattern.search(ip_add_range_entered):
            print(f"{ip_add_range_entered} is a valid ip address range")
            break


    # Try ARPing the ip address range supplied by the user. 
    # The arping() method in scapy creates a pakcet with an ARP message 
    # and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
    # If a valid ip address range was supplied the program will return 
    # the list of all results.
    arp_result = scapy.arping(ip_add_range_entered)
    # print("\n* credit https://www.youtube.com/davidbombal                   *")

# ------------------------------------------------------------------------------------
else:
    
    os.system("cls")
    old = time.time()
    print("Please enter a valid OPTION !!!")
    os.system("pause")
    current = time.time()

    os.system("cls")
    print(f'Time taken is {current-old}')
 

