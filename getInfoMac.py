from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from selenium.common.exceptions import NoSuchElementException


def help():
    print("""
    Usage: python3 getInfoMac.py <your macs file(.txt)>
    """)


def get():
    # Create a webdriver instance
    #firefox_options = Options()
    #firefox_options.add_argument('--headless')
    browser = webdriver.Firefox()
    #mac_input = browser.find_element_by_id('ml_mac_add')


    # Open the MAC addresses file
    macs = open(sys.argv[1], "r")
    lines = macs.readlines()
    for line in lines:
        try:
            # Visit the MAC lookup website
            browser.get("https://dnschecker.org/mac-lookup.php?query={}".format(line))
            
            # Find and click the submit button
            submit_button = browser.find_element_by_id('ml_submit')
            submit_button.click()
            
            time.sleep(3)
            
            # Find the element containing the corporation information
            temp = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[3]/table/tbody/tr[2]/td[2]")
            
            # Print the MAC address and corporation information
            print("\n", line, "Corporation: ", temp.text)
        
        except NoSuchElementException as e:
            # Handle the case when the information is not found
            print("[!] {} Information Not Found:".format(line))
    
    # Quit the browser
    browser.quit()


# Call the get function
get()
