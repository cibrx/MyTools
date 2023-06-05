import psutil

class GetIface(object): 
    def getInterfaceName(self):
        # Get network interface addresses
        addrs = psutil.net_if_addrs()
        print("[*]Interface Names:")
        
        temp = 1
        for inter in addrs:
            print(str(temp) + ". :==: " + str(inter))  # Display interface names
            temp += 1
        
        temp = 1
        iface = int(input("Please Choose An Interface Number :==: "))  # Prompt user to choose an interface number
        
        for inter in addrs:
            if temp == iface:
                print("Selected Interface: ", inter)  # Display the selected interface
                return inter
            temp += 1
