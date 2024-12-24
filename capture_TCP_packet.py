#!/usr/bin/env python3
# Task 1.2--------------------------------


from scapy.all import *


def print_pkt(pkt):
  print_pkt.num_packets +=1
  print("\n======================= packet: {} =========================\n".format(print_pkt.num_packets))

print_pkt.num_packets = 0

# The interface can be found with
# 'docker network ls' in the VM
# or 'ifconfig' in the container
# 1.1.Capture only ICMP packet
# pkt = sniff(iface='br-6d54bbcb5aeb', filter='icmp', prn=print_pkt)


# 1.2. Capture any TCP packet that comes from a particular IP and with a destination port number 23.

pkt = sniff(iface='br-6d54bbcb5aeb', filter='tcp && src host 10.9.0.6 && dst port 23', prn=print_pkt)
