# -*- coding: utf-8 -*-
import scrapy
from qczj.items import QczjItem


class Bw5Spider(scrapy.Spider):
    name = 'bw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/photolist/series/65/10/p1/?pvareaid=101197']

    def parse(self, response):
        divs = response.xpath("//div[@class='js-grid-main column grid-main']/div")[1:3]
        for div in divs:
            urls = div.xpath("./ul/li/a/img/@src").getall()
            for url in urls:
                img_url = response.urljoin(url)
                item = QczjItem(urls=img_url)
                yield item





if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrpay crawl bw5".split())