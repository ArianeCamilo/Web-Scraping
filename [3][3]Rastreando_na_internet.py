from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#Recupera uma lista de todos os links internos encontrados em uma página
def getInternalLinks(bsObj, includeUrl):
	internalLinks = []
	#Encontra todos os links que começam com a "/"
	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs["href"] is not None:
			if link.attrs["href"] not in internalLinks:
				internalLinks.append(link.attrs["href"])
	return internalLinks

#Recupera uma lista com todos os links externos encontrados em uma página
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	#Encontra todos os links que começam com "http" ou "www" que não contêm
	#o URL atual
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs["href"] is not None:
			if link.attrs["href"] not in externalLinks:
				externalLinks.append(link.attrs["href"])
	return externalLinks

def splitAddress(address):
	addressParts = address.replace("http://", "").split("/")
	return addressParts

def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bsObj = BeautifulSoup(html, "lxml")
	externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
	if len(externalLinks) == 0:
		internalLinks = getInternalLinks(startingPage)
		return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])

	else: 
		return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink("http://oreilly.com")
	print("Random external link is: " + externalLink)


#Coleta uma lista de todos os URLs externos encontrados no site
allExtLinks = set()
allIntLinks= set()
def getAllExternalLinks(siteUrl):
        html = urlopen(siteUrl)
        bsObj = BeautifulSoup(html, "lxml")
        internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
        externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
        for link in externalLinks:
        	if link not in allExtLinks:
        		allExtLinks.add(link)
        		print(link)

        for link in internalLinks:
        	if link not in allIntLinks:
        		print("About to get link: " + link)
        		allIntLinks.add(link)
        		getAllExternalLinks(link)

getAllExternalLinks("http://oreilly.com")
        
followExternalOnly("http://oreilly.com")


