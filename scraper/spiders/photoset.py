# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scraper.items import PhotoSetItem
import re


class PhotoSetSpider(CrawlSpider):
    name = 'photoset'
    allowed_domains = ['www.shzx.org']
    start_urls = [
        'https://www.shzx.org/b/162-0.html', 
        'https://www.shzx.org/b/163-0.html',
        'https://www.shzx.org/b/168-0.html',
        'https://www.shzx.org/b/167-0.html',
        'https://www.shzx.org/b/165-0.html',
        'https://www.shzx.org/b/169-0.html',
        'https://www.shzx.org/b/172-0.html',
        'https://www.shzx.org/b/173-0.html',
        'https://www.shzx.org/b/175-0.html', 
        'https://www.shzx.org/b/177-0.html',
        'https://www.shzx.org/b/148-0.html',
        'https://www.shzx.org/b/82-0.html',
        'https://www.shzx.org/b/160-0.html',
    ]

    rules = [
        Rule(LinkExtractor(allow=(r'/a/\d+-\d+-0\.html'),
            allow_domains=('www.shzx.org')), 
            callback='parse_item', 
            follow=True
        ),
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'scraper.pipelines.PhotoSetPipeline': 300,
        }
    }

    def parse_item(self, response: Response):
        item = PhotoSetItem()
        item['title'] = response.xpath('//div[@class="title"]/h1/text()').extract()[0]
        info = response.xpath('//div[@class="info"]/left/text()').extract()[0]
        item['datetime_published'], item['author'], item['source'] = [e[3:] for e in re.split(r'\xa0+', info)]
        item['url'] = response.url
        item['tags'] = '/'.join(response.xpath('//div[@class="tags"]/a[@target="_blank"]/text()').extract())
        item['description'] = response.xpath('//div[@class="text"]/text()').extract()[0]
        yield item
