from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
import config


class BrokenItem(Item):
    status = Field()
    url = Field()
    referer = Field()

class GoodItem(Item):
    status = Field()
    url = Field()
    referer = Field()

class BrokenLinksSpider(CrawlSpider):
    name = config.name
    allowed_domains = config.allowed_domains
    start_urls = config.start_urls
    handle_httpstatus_list = [404]
    rules = (Rule(LinkExtractor(tags=(config.tags), allow=(config.match)), callback='parse_item', follow=config.follow),)

    def parse_item(self, response):
        if response.status == 200 and config.show_passed == True:
            item = GoodItem()
            item['status'] = response.status
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')

            return item
        elif response.status == 404:
            item = BrokenItem()
            item['status'] = response.status
            item['url'] = response.url
            item['referer'] = response.request.headers.get('Referer')

            return item
