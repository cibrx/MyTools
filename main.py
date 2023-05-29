import os
import sys
import socket
from datetime import datetime
import os
import scapy.all as scapy
import getIface

class MyTools(object):

	def __init__(self):
	
		self.menu="""
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
			\n[0]-Exit\n[1]-Port Scanner\n[2]-Network Sniffer"""
		
	# Defining a target
	def PortScanner(self):
		target = input("[?]Target Ip: ")    
		device = input("[?]Device Name: ")
		ipchange = input("[?]Do you want spoof MAC address?[Enter default =y/N]")
		writeLogs=input("[?]Do you want to write the output somewhere?If (yes) write file name Else Press ENTER :==: ")
		
		if ipchange == "":
			os.system("ifconfig "+device+" down")
			os.system("macchanger -r "+device)
			os.system("ifconfig "+device+" up")
		# Add Banner
		print("[*]Scanning Target: " + target)
		print("[*]Scanning started at:" + str(datetime.now()))
		print("-" * 50)

		try:
			# will scan ports between 1 to 65,535
			for port in range(1,65535):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				
				# returns an error indicator
				result = s.connect_ex((target,port))
				if result == 0 and writeLogs=="":
					output="[*]Port {} is open".format(port)
					print(output)

				elif result == 0 and writeLogs!="":
					logFile = open("log_files/+{}+.txt".format(writeLogs),"w")
					logFile.write(output)
					
				s.close()
				
		except KeyboardInterrupt:
				print("\n [*]Exiting Program !!!!")
				sys.exit()
		except socket.gaierror:
				print("\n [*]Hostname Could Not Be Resolved !!!!")
				sys.exit()
		except socket.error:
				print("\ [*]Server not responding !!!!")
				sys.exit()

		
	def NetworkSniffer(self):
		result = getIface.GetIface.getInterfaceName(self)
		os.system("clear")
		print("Passive Network Scanner Open\nMac Address"+38*(" ")+"Ip Address\n"+59*"*")
		ipaddress = []

		while True:
			s = scapy.AsyncSniffer(iface = result, filter = 'arp', count = 5)
			s.start()
			s.join()
			pkts = s.results

			for p in pkts:
				if p.op == 2 and not str(p.pdst) in ipaddress:
					ipaddress.append(str(p.pdst))
					print(p.hwdst+38*(" ")+p.pdst)
	
		