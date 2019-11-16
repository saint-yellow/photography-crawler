# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scraper.items import PhotoItem
import re


class PhotoSpider(CrawlSpider):
    name = 'photo'
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
        Rule(LinkExtractor(allow=(r'/a/\d+-\d+-\d+\.html'),
            allow_domains=('www.shzx.org')), 
            callback='parse_item', 
            follow=True
        ),
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'scraper.pipelines.PhotoPipeline': 400,
        }
    }

    def parse_item(self, response: Response):
        item = PhotoItem()
        title = response.xpath('//div[@class="title"]/h1/text()').extract()[0]
        item['title'] = title
        item['webpage_url'] = response.url
        item['notation'] = re.findall(r'\d+-\d+', response.url)[0]
        item['photo_urls'] = response.xpath('//div[@class="picture"]/p/img[@alt="{0}"]/@src'.format(title)).extract()
        return item
