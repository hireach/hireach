# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-zA-Z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self,response):
        title = response.xpath("//h1[@class='title']/text()").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get()
        url = response.url
        url1 = url.split("?")[0]
        acticle_id = url1.split('/')[-1]
        content = response.xpath("//div[@class='show-content']").get()

        # seleniumm获得的数据
        wordage = response.xpath("//span[@class='wordage']/text()").get()
        likes_count = response.xpath("//span[@class='likes-count']/text()").get()

        item = JianshuSpiderItem(title=title,author=author,pub_time=pub_time,acticle_id=acticle_id,content=content)
        yield item


if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrpay crawl js".split())