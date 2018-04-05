from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import datetime
import random
import re

random.seed(datetime.datetime.now())  # config o seed do gerador de nºs aleatórios com a hora atual do sistema
# para assegurar um novo caminho aleatório a cada vez q o prog é executado


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = bs(html, "lxml")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Belchior")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)