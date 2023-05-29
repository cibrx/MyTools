import psutil

class GetIface(object): 
    def getInterfaceName(self):
            
            addrs = psutil.net_if_addrs()
            print("[*]Interface Names:")
            temp=1
            for inter in addrs:
                print(str(temp)+". :==: "+str(inter))
                temp+=1
            temp=1
            iface = int(input("Please Choose A Interface Number :==: ")	)
            for inter in addrs:
                if temp == iface:
                    return inter