from scrapy.crawler import CrawlerProcess
from scraper.spiders.photo import PhotoSpider
from scraper.spiders.photoset import PhotoSetSpider
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(PhotoSetSpider)
process.crawl(PhotoSpider)
process.start()