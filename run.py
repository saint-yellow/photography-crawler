from scrapy.crawler import CrawlerProcess
from scraper.spiders.photo import PhotoSpider
from scraper.spiders.photoset import PhotoSetSpider
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
process = CrawlerProcess(settings)

# 采集图片相关文本信息
process.crawl(PhotoSetSpider)

# 采集图片文件
process.crawl(PhotoSpider)

process.start()