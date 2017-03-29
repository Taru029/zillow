# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    links = scrapy.Field()
    address = scrapy.Field()
    lat_long = scrapy.Field()
    price = scrapy.Field()
    specs = scrapy.Field()
    day_on_zillow = scrapy.Field()
    image = scrapy.Field()
    #pass

class LiveProItem(scrapy.Item):
    url = scrapy.Field()
