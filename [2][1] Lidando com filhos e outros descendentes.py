from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = bs(html, "lxml")

for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)