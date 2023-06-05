from main import MyTools

class Execute(MyTools):
    def Run(self):
        mytools = MyTools()
        while True:
            try:
                print("*" * 50)
                # Display the menu
                print(mytools.menu)
                print("*" * 50)
                select = int(input("[?] Please, select a function:==: "))
                
                if select == 1:
                    # Call the PortScanner method from MyTools class
                    MyTools.PortScanner(self)
                elif select == 2:
                    # Call the NetworkSniffer method from MyTools class
                    MyTools.NetworkSniffer(self)
                elif select == 0:
                    print("Bye")
                    break
            except KeyboardInterrupt:
                print("If you want to exit, press (0)...")
                continue
        
e = Execute()
e.Run()
