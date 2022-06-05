# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
class Imoveis(Item):
    # define the fields for your item here like:
    vivaId = Field()
    account = Field()
    listing = Field()
    medias = Field()
    link = Field()
        