import requests
import re
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LagouSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=sug&suginput=p"
        self.position = []

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            # 页面一直循环，直到 id="myDynamicElement" 出现
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='pager_container']/span[last()]"))
            )
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            if "pager_next pager_next_disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
            time.sleep(1)

    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self,url):
        self.driver.get(url)
        source = self.driver.page_source
        self.parse_detail_page(source)

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        ps_name = html.xpath("//h2[@class='fl']/em/text()")[0]
        job_req = html.xpath("//div[@class='job-detail']/p")
        posision = {
            "ps_name":ps_name,
            "job_req":job_req
        }
        self.position.append(posision)
        print(job_req)
        print('*'*49)


if __name__ == '__main__':
    pass