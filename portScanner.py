import os
import pyfiglet
import sys
import socket
from datetime import datetime
menu="""
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
    / ***********  \                        / ***********  \ 
  --------------------                    --------------------\n[0]-Exit\n[1]-Port Scanner\n[2]-Arp Spoofer"""
# Defining a target

def PortScanner():
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

while True:
    print("*" * 50)
    ascii_banner = pyfiglet.figlet_format("[*] LegendMan46")
    print(ascii_banner)
    print(menu)
    print("*" * 50)
    select=int(input("[?]Please,Select a Function :==: "))
    
    if select == 1:PortScanner()
    elif select == 0:print("bye");break
    
        
























