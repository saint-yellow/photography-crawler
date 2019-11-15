# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhotoSetItem(scrapy.Item):
    '''相片集'''

    title = scrapy.Field()
    datetime_published = scrapy.Field()
    author = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
    description = scrapy.Field()


class PhotoDetailItem(scrapy.Item):
    '''相片'''

    title = scrapy.Field()
    webpage_url = scrapy.Field()
    notation = scrapy.Field()
    photo_urls = scrapy.Field()
