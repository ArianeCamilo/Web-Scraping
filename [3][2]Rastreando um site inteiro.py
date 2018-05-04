from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                #Encontramos uma página nova
                newPage = link.attrs["href"]
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("") 

# A tendência deste crawler é travar, pois o limite de recursão padrão do Python é 1000.
# Como a rede de links da Wikipédia é muito grande, este crawler atingirá o limite e será interrompido
# Este método funciona para sites com menos e 1000 links de profundidade