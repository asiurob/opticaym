import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class Spider( scrapy.Spider ):
	name="project"
	links = []
	start_urls = links

	def __init__( self, l ):
		self.links.append( l )

	def parse( self, response ):
		for item in response.xpath('//a'):
			print(item)


class initCrawl:
	def __init__( self, link ):
		configure_logging()
		crawler = CrawlerRunner()
		crawler.crawl( Spider )
		d = crawler.join()
		d.addBoth( lambda _: reactor.stop() )
		reactor.run()
