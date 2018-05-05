# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class Article(Item):
	# defina os campos do seu item aqui, como:
	# name = scrapy.Field()
	title = Field()


# Cada objeto "Item" do Scrapy representa uma única página do site.
# Pode-se definir quantos campos quiser (url, header image, content etc.)