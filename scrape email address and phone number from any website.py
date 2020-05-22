import re              # this provide format that needs to be scraped
import time            # it make the program to sleep for specific time 

from urllib.request import Request, urlopen  # this get the html ,act like headless browser
from bs4 import BeautifulSoup
print("ENTER THE URL TO FIND MOBILE NUMBER AND EMAIL url eg:https://www.homersbrandcare.com")     # url of website from which we need email and phone number

url=str(input())
req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
html = urlopen(req).read()
html=html.decode()
bsObj = BeautifulSoup(html,features="lxml");
links=[]
for link in bsObj.find_all('a'):
    links.append(str(link.get('href')))
    #print(url + str(link.get('href')))


def Email(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        hh = urlopen(req).read()       # we are making request act like firefox browser
        time.sleep(0.5)
        #time.sleep(1)
    #raw_html=t.text
    #dd=html2text.html2text(hh)
        dd=hh.decode()                                              
        email=re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',dd)   # this is the format ,based on this format only we will get results
                                                                                                                    # this is email format
        print(email)
        phone=re.findall(r'(tel\s?:?[0-9]+)|(\+91-?[0-9]+)',dd)   # phone number format
        print(phone)
    #links.remove(url)
    except:
       pass
for b in links:
    Email(b)
    time.sleep(0.5)
    
