# !/usr/bin/env python

import scapy.all as scapy 

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packer = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packer/arp_packet
    answerd_list = scapy.srp(arp_broadcast_packet, 1, verbose=False)[0]
    client_list = []

    for element in answerd_list:
        client_dict = {"ip" : element.psrc, "mac" : element.hwsrc}
        client_list.append(client_dict)

    return client_list

result_list = scan("10.0.2.1/24")