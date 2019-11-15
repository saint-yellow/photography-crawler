# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .database import engine, Session, PhotoSet
from .items import PhotoSetItem, PhotoDetailItem
from scrapy import Spider
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from datetime import datetime
import arrow
from scrapy.exceptions import DropItem
import os

class PhotoSetPipeline(object):
    def __init__(self):
        self.session = Session()

    def process_item(self, item, spider: Spider):
        record = PhotoSet(
            url=item['url'],
            title=item['title'], 
            author=item['author'],
            source=item['source'], 
            datetime_published=item['datetime_published'],
            description=item['description'],
            tags=item['tags'])
        self.session.add(record)
        self.session.commit()
        
    def close_spider(self, spider: Spider):
        self.session.close()


class PhotoPipeline(ImagesPipeline):
    def get_media_requests(self, item: PhotoDetailItem, info):
        for photo_url in item['photo_urls']:
            yield Request(photo_url, meta={'name': item['notation']}, headers={'Referer': item['webpage_url']})

    def file_path(self, request: Request, response=None, info=None):
        photo_extension = request.url.split('.')[-1]
        file_name = request.meta['name'] + '-' + str(arrow.get(datetime.now()).timestamp) + '.' + photo_extension
        return os.path.join(request.meta['name'], file_name)

    def item_completed(self, results, item, info):
        print(results)
        photo_paths = [x['path'] for ok, x in results if ok]
        if not photo_paths:
            raise DropItem("Item contains no photos")
        item['photo_urls'] = photo_paths
        return item
