# A função next_siblings() do BeautifulSoup facilita a coleta de dados em tabelas,
# principalmente as que têm linhas de título

from urllib.request import urlopen
from bs4 import BeautifulSoup as bp

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = bp(html, "lxml")

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

    # não captura os irmãos do título (função excludente), apenas as linhas seguintes