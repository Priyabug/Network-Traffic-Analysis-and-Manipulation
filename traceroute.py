#!/usr/bin/env python3

from scapy.all import *

inRoute = True
i = 1
while inRoute:

      a=IP(dst='216.58.210.36', ttl=i)
      response = srl(a/ICMP(), timeout=7,verbose=0)

      if response is None:
            print(f*{i} {response.src}")
            inRoute = False
       
      else:
            print(f*{i} {response.src}") 

     i=i+1  
