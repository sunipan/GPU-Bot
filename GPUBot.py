from bs4 import BeautifulSoup as bs
import ctypes
import webbrowser
import requests
import time
import timeit
from lxml import html
from datetime import datetime

# Desired website urls
links = {'3070 FE':'https://bit.ly/3ebHiSm',
         '3070 EVGA':'https://bit.ly/3tGV1Ha',
         '3060Ti FE':'https://bit.ly/3v4uYtM',
         '3080 EVGA':'https://bit.ly/3tGUGnS'}
testURL = 'https://bit.ly/3tAivxy'
# Path to chrome on local machine (don't forget to add '%s')
chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# Different user agents to limit potential of getting banned by best buy
headers1 = {'user-agent':'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36'}
headers2 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
headers3 = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:88.0) Gecko/20100101 Firefox/88.0'}
headers4 = {'user-agent':'Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0'}
headers5 = {'user-agent':'Mozilla/5.0 (Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}
headers6 = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0'}
headers7 = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}
headers8 = {'user-agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}
headers9 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
headers10 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
headers11 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
headers12 = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
headers13 = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1'}

# Initialize the headers
headers = []
for i in range(1,14):
    headers.append(globals()['headers' + str(i)])
    print('ADDING HEADER: ' + str(headers[i-1]))
print('========================================================\n')
headerSelect = 0
start = time.time()
while(True):
    # Iterate through the links
    for key in links:
        # Scrape the page
        end = time.time()
        if end - start > 36000:
            ask = ctypes.windll.user32.MessageBoxW(0, "Change IP", "Warning", 1)
            start = time.time()
            if ask == 2:
                break
        page = requests.get(links[key], headers=headers[headerSelect])
        if str(page) == '<Response [200]>':
            print('Scrape Status for ' + key + ': Success')
        else:
            print('Status for ' + key + ': ' + str(page))
        soup = bs(page.text, 'lxml')
        # Simple link iterator variable
        headerSelect += 1
        if headerSelect == 13:
            headerSelect = 0

        # Availability of card on bestbuy.ca
        avail = soup.find(class_='availabilityMessage_ig-s5 container_3LC03').decode_contents()
        print('Availability of ' + key + ': ' + avail + ' | Time: ' + datetime.now().strftime("%H:%M:%S")+'\n')
        print('========================================================\n')
        if avail != 'Coming soon' and avail != 'Sold out online':
            # If in stock, open the web page to it!
            webbrowser.get(chromePath).open(links[key])
    # Delay program to not spam the site, decrease or remove at your own risk
    time.sleep(10)


