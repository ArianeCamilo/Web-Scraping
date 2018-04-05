from urllib.request import urlopen
from bs4 import BeautifulSoup as bp

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = bp(html, "lxml")

print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
# retorna o preço do objeto representado pela imagem localizada em "../img/gifts/img1.jpg"
# selecionando o irmão anterior (previous_sibling) da tag pai (td) de onde a img está
