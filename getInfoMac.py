import sys
import random
import requests
from datetime import datetime

def help():
    print("""
    Usage: python3 getInfoMac.py <your mac file(.txt)>
    """)


def get():
    # Open the MAC addresses file
    macs = open(sys.argv[1], "r")
    lines = macs.readlines()

    # get csrf token
    csrf = requests.get('https://dnschecker.org/ajax_files/gen_csrf.php?upd=' + str(random.random() * 1000 + datetime.now().microsecond // 1000), headers={'Referer': 'https://dnschecker.org/mac-lookup.php?query=00000000000'})

    for line in lines:
        # send query with csrf token
        data = requests.post('https://dnschecker.org/ajax_files/mac_lookup.php', headers={'Content-Type': 'application/x-www-form-urlencoded', "csrftoken": csrf.json().get('csrf'), 'Referer': 'https://dnschecker.org/mac-lookup.php?query=000000000000'}, data={'mac_add': line.strip()})

        # if there is something in errors array print it out, if not print the result and mac address
        if data.text == "Invalid CSRF.":
            print("[!] Invalid CSRF Token")
        elif data.json().get('errors'):
            print(data.text)
            print("[!] Information Not Found:", line.strip())
        else:
            print(line.strip(), "Corporation:", data.json().get('result')[0].get('name'))

# Call the get function
get()
