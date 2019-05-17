from lxml import etree
from queue import Queue
from urllib import request
import requests
import threading
import os
import re


class Producter(threading.Thread):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    def __init__(self,paga_queue,img_queue,*args,**kwargs):
        super(Producter,self).__init__(*args,**kwargs)
        self.page_queue = paga_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url,headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get("data-original")
            img_title = img.get('alt')
            alt = re.sub(r'[\?？\.。@，""@“”!！]','',img_title)
            # 获取文件名后缀
            suffix = os.path.splitext(img_url)[1]
            filename = alt + suffix
            self.img_queue.put((img_url,filename))


class Consumer(threading.Thread):
    # 加请求头就可以了
    opener = request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')]
    request.install_opener(opener)
    def __init__(self,paga_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = paga_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            print(img_url)
            request.urlretrieve(img_url,'images/'+filename)
            print("下载完成")

def main():
    page_queue = Queue(100)
    img_queue =Queue(500)
    for x in range(1,30):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        page_queue.put(url)
    for i in range(5):
        t = Producter(page_queue,img_queue)
        t.start()
    for i in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()


if __name__ == '__main__':
    main()