# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BonbanhItem(scrapy.Item):
    date = scrapy.Field()
    url = scrapy.Field()
    brand = scrapy.Field()
    serie = scrapy.Field()
    model_year = scrapy.Field()
    info = scrapy.Field()
    price_vnd = scrapy.Field()
    price_dol = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    description = scrapy.Field()
