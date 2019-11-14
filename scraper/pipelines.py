# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .database import engine, Session, PhotoCollection, PhotoDetail
from .items import PhotoCollectionItem, PhotoDetailItem
from scrapy import Spider
from scrapy.pipelines.images import ImagesPipeline

class SihaizixunPipeline(object):
    def __init__(self):
        self.session = Session()


    def open_spider(self, spider):
        pass


    def process_item(self, item, spider: Spider):
        if isinstance(item, PhotoCollectionItem):
            photo_collection = PhotoCollection(
                url=item['url'],
                title=item['title'], 
                author=item['author'],
                source=item['source'], 
                datetime_published=item['datetime_published'],
                description=item['description'],
                tags=item['tags'])
            self.session.add(photo_collection)
            self.session.commit()
        if isinstance(item, PhotoDetailItem):
            photo_infomation = PhotoDetail(
                title=item['title'],
                webpage_url=item['webpage_url'],
                photo_url=item['photo_url'])
            self.session.add(photo_infomation)
            self.session.commit()
        

    def close_spider(self, spider: Spider):
        self.session.close()


class PhotoDownloadingPipeline(ImagesPipeline):
    def __int__(self):
        pass

    def open_spider(self, spider: Spider):
        pass

    def process_item(self, item: PhotoDetailItem, spider: Spider):
        pass

    def close_spider(self):
        pass

    def item_completed(self, results, item, info):
        pass

    def get_images(self, response, request, info):
        pass

    def get_media_requests(self, item, info):
        pass
