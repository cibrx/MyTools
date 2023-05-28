from main import MyTools

class Execute(MyTools):
    def Run(self):
        mytools=MyTools()
        while True:
            try:
                print("*" * 50)
                print(mytools.menu)
                print("*" * 50)
                select=int(input("[?]Please,Select a Function :==: "))
                
                if select == 1:MyTools.PortScanner()
                elif select== 2:MyTools.NetworkSniffer(self)
                elif select == 0:print("bye");break
            except KeyboardInterrupt:
                print("If you want to exit,press (0)...")
                continue
        
e=Execute()
e.Run()

















