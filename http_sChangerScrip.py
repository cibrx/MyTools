import mitmproxy

def request(flow):
    print(flow)
    if flow.response.headers.get("content-type", "").startswith("image"):
        img = open("ihackedyou.png", "rb").read()
        flow.response.content = img
        flow.response.headers["content-type"] = "image/png"
    
