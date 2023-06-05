import os
import sys
import socket
from datetime import datetime
import os
import scapy.all as scapy
import getIface
import random

class MyTools(object):

	def __init__(self):
		self.menu = """
			 __      __    _                              _ __  __             _  _    __   
			| _|_/\_|_ |  | |    ___  __ _  ___ _ __   __| |  \/  | __ _ _ __ | || |  / /_  
			| |\    /| |  | |   / _ \/ _` |/ _ \ '_ \ / _` | |\/| |/ _` | '_ \| || |_| '_ \ 
			| |/_  _\| |  | |__|  __/ (_| |  __/ | | | (_| | |  | | (_| | | | |__   _| (_) |
			| |  \/  | |  |_____\___|\__, |\___|_| |_|\__,_|_|  |_|\__,_|_| |_|  |_|  \___/ 
			|__|    |__|            |___/                                                  
			
			 _______________                        |*\_/*|________
			|  ___________  |     .-.     .-.      ||_/-\_|______  |
			| |           | |    .****. .****.     | |           | |
			| |   0   0   | |    .*****.*****.     | |   0   0   | |
			| |     -     | |     .*********.      | |     -     | |
			| |   \___/   | |      .*******.       | |   \___/   | |
			| |___     ___| |       .*****.        | |___________| |
			|_____|\_/|_____|        .***.         |_______________|
			  _|__|/ \|_|_.............*.............._|________|_
			 / ********** \                          / ********** \ 
			/  *********** \                        / ***********  \ \n 
			\n[0]-Exit\n[1]-Port Scanner\n[2]-Network Sniffer(Support Only Wireless)"""

	def PortScanner(self):
		target = input("[?]Target Ip: ")    
		device = str(getIface.GetIface.getInterfaceName(self))
		ipchange = input("\n[?]Do you want to spoof MAC address? !!NOT RECOMMENDED!! [Enter default = No [y/N]")
		writeLogs = input("[?]Do you want to write the output somewhere? If yes, write file name, else press ENTER: ==: ")
		if ipchange.upper() == "Y":
			os.system("ifconfig " + device + " down")  # Disable the network interface
			os.system("macchanger -r " + device)  # Randomize the MAC address
			os.system("ifconfig " + device + " up")  # Enable the network interface
		print("[*]Scanning Target: " + target)
		print("[*]Scanning started at: " + str(datetime.now()))
		print("-" * 50)

		try:
			for port in range(1, 65535):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				result = s.connect_ex((target, port))
				if result == 0:
					output = "[*]Port {} is open".format(port)
					print(output)
					if writeLogs != "":
						logFile = open("log_files/log_{}.txt".format(writeLogs), "a+")  # Open the log file in append mode
						logFile.write(output + "\n")  # Write the output to the log file
					s.close()
		except KeyboardInterrupt:
			print("\n[*]Leaving the program!!!")
			sys.exit()
		except socket.gaierror:
			print("\n[*]Hostname could not be resolved!!!")
			sys.exit()
		except socket.error:
			print("\n[*]Server not responding!!!")
			sys.exit()

	def NetworkSniffer(self):
		result = getIface.GetIface.getInterfaceName(self)
		os.system("clear")
		info = input("Do you want to save MAC addresses? [Y/n]")
		if info == "" or info.upper() == "Y":
			temp = random.randint(10, 100)
			f = open("macFolder/macAddress_{}.txt".format(temp), "a+")  # Open a file to save MAC addresses
			print("Your file ID number: {}".format(temp))
		print("Passive Network Scanner Open\nMac Address" + 38 * " " + "Ip Address\n" + 59 * "*")
		ipaddress = []
		while True:
			s = scapy.AsyncSniffer(iface=result, filter='arp', count=5)  # Sniff ARP packets
			s.start()
			s.join()
			pkts = s.results

			for p in pkts:
				if p.op == 2 and not str(p.pdst) in ipaddress:  # Check if it's a response and if the IP address is not already recorded
					ipaddress.append(str(p.pdst))
					print(p.hwdst + 38 * " " + p.pdst + 12 * " ")
					if info == "" or info.upper() == "Y":
						f.write(p.hwdst + "\n")  # Write the MAC address to the file
