# -*- coding: utf-8 -*-
import scrapy


class Renre1Spider(scrapy.Spider):
    name = 'renre1'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {"email":"19925975560","password":"yqa18879753003"}
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request

    def parse_page(self,response):
       print(response.text)

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrpay crawl renre1".split())