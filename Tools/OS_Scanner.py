#!/usr/bin/env python3
import os
import platform
import socket

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
    print("\n* Muhammad Rafi Ediananta                                      *")
    print("\n* OS Scanner Tools                                             *")
    print("\n****************************************************************\n")
    net_ip = input("Input The IP : ")
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