# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, Response
from ..items import PhotoCollectionItem, PhotoDetailItem
import re


class SihaizixunSpider(scrapy.Spider):
    storage_folder = 'shzx.org'
    home_url = 'https://www.shzx.org'
    name = 'sihaizixun'
    allowed_domains = ['www.shzx.org']
    photo_collection_urls = []
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

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_gallery)


    def parse_gallery(self, response: Response):
        collection_pages = response.xpath('//div[@class="b_img"]/ul/li/a[@target="_blank"]/@href').extract()
        for page in collection_pages:
            yield Request(self.home_url+page, callback=self.parse_photographic_work)
        next_page = response.xpath('//div[@class="paging"]/a[text()="下一页"]/@href').extract()
        if next_page is not None and len(next_page) >= 1:
            yield Request(self.home_url+next_page[0], callback=self.parse_gallery, dont_filter=False)


    def parse_photographic_work(self, response: Response):
        if response.url.endswith('-0.html'):
            pci = PhotoCollectionItem()
            pci['title'] = response.xpath('//div[@class="title"]/h1/text()').extract()[0]
            info = response.xpath('//div[@class="info"]/left/text()').extract()[0]
            pci['datetime_published'], pci['author'], pci['source'] = [e[3:] for e in re.split(r'\xa0+', info)]
            pci['url'] = response.url
            pci['tags'] = response.xpath('//div[@class="tags"]/text()').extract()[0].replace('关键词：', '')
            pci['description'] = response.xpath('//div[@class="text"]/text()').extract()[0]
            yield pci

        title = response.xpath('//div[@class="title"]/h1/text()').extract()[0]
        photo_urls = response.xpath('//div[@class="picture"]/p/img[@alt="{0}"]/@src'.format(title)).extract()
        for url in photo_urls:
            pdi = PhotoDetailItem()
            pdi['title'] = title
            pdi['webpage_url'] = response.url
            pdi['photo_url'] = url
            yield pdi

        next_page = response.xpath('//div[@class="paging"]/a[text()="下一页"]/@href').extract()
        if next_page is not None and len(next_page) >= 1:
            yield Request(self.home_url+next_page[0], callback=self.parse_photographic_work)


    

