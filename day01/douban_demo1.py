# coding:utf-8

from lxml import etree
import requests

url = "https://movie.douban.com/cinema/nowplaying/shenzhen/"
headers = {
    "Referer": "https://movie.douban.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

response = requests.get(url,headers=headers)
res = response.content.decode('utf-8')
html = etree.HTML(res)
lis = html.xpath("//div[@id='nowplaying']/div[2]/ul/li")
items = []
#print(etree.tostring(lis,encoding='utf-8').decode('utf-8'))
for li in lis:
    item = {}
    item["name"] = li.xpath("@data-title")[0]
    item["director"] = li.xpath("@data-director")
    item["region"] = li.xpath("@data-region")[0]
    item["actors"] = li.xpath("@data-actors")
    item["category"] = li.xpath("@data-category")[0]
    item["score"] = li.xpath("@data-score")[0]
    item["上映时间"] = li.xpath("@data-release")[0]
    item["img"] = li.xpath(".//li[@class='poster']/a/@href")[0]
    item["href"] = li.xpath(".//li[@class='poster']/a//@src")[0]
    items.append(item)
print(items)