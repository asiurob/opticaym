import scrapy
from scrapy.crawler import CrawlerProcess

class Spider( scrapy.Spider ):

process = CrawlerProcess({'USER_AGENT' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
process.crawl( Spider )
process.Start()
