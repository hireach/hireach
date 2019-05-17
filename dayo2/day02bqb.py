import requests
from lxml import etree
import urllib.request
import os
import re


def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get("data-original")
        img_title = img.get('alt')
        print(img_title)
        alt = re.sub(r'[\?？\.。@，""@“”!！]','',img_title)
        # 获取文件名后缀
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        urllib.request.urlretrieve(url=img_url,filename='images/'+filename)

def main():
    for i in range(30):
        url = 'http://www.doutula.com/photo/list/?page=%d' % i
        parse_page(url)
        break


if __name__ == '__main__':
    main()