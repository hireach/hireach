# coding:utf-8

from lxml import etree
import requests


BASE_URL = "http://www.ygdy8.net/"
headers = {
    #"Referer": "https://movie.douban.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

def get_detail_urls(url):
    response = requests.get(url,headers=headers)
    res = response.content.decode('gbk')
    #print(response.url)
    html = etree.HTML(res)

    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_URL+url,detail_urls)
    return detail_urls


def parse_movie(url):
    """
     ◎译名      : ◎译\u3000\u3000名\u3000疾速特攻/杀神John Wick 2(港)/捍卫任务2(台)/疾速追杀2/极速追杀：第二章/约翰·威克2
        ◎片名      : ◎片\u3000\u3000名\u3000John Wick: Chapter Two
        ◎年代　    : ◎年\u3000\u3000代\u30002017
        ◎国家　    : ◎产\u3000\u3000地\u3000美国
        ◎类别　    : ◎类\u3000\u3000别\u3000动作/犯罪/惊悚
        ◎语言　    : ◎语\u3000\u3000言\u3000英语
        ◎字幕　    : ◎字\u3000\u3000幕\u3000中英双字幕
        ◎上映日期  ：◎上映日期\u30002017-02-10(美国)
        ◎IMDb评分  : ◎IMDb评分\xa0 8.1/10 from 86,240 users
        ◎豆瓣评分　 : ◎豆瓣评分\u30007.7/10 from 2,915 users
        ◎文件格式   : ◎文件格式\u3000x264 + aac
        ◎视频尺寸　 : ◎视频尺寸\u30001280 x 720
        ◎文件大小　 : ◎文件大小\u30001CD
        ◎片长　    : ◎片\u3000\u3000长\u3000122分钟
        ◎导演　    : ◎导\u3000\u3000演\u3000查德·史塔赫斯基 Chad Stahelski
        ◎主演　    :
    :param url:
    :return:
    """
    response = requests.get(url, headers=headers)
    res = response.content.decode('gbk')
    # print(response.url)
    html = etree.HTML(res)
    movie = {}
    movie["title"] = html.xpath("//font[@color='#07519a']/text()")[0]
    movie["public_data"] = html.xpath("//div[@class='co_content8']/ul/text()")[0].strip()
    movie["cover"] = html.xpath("//div[@id='Zoom']//img[1]/@src")[0]
    movie["screenshot"] = html.xpath("//div[@id='Zoom']//img/@src")[1]
    movie["screenshot"] = html.xpath("//div[@id='Zoom']//img/@src")[1]
    content = html.xpath("//div[@class='co_content8']/ul/tr/td/div/td/p/text()")
    # 类型
    item = []
    for index,info in enumerate(content):
        if info.startswith("◎") or info.startswith("\u3000"):
            if not info.startswith("◎片\u3000\u3000名"):
                item.append(info)
    #print(item)
    actor = ''
    for each in item:
        if each[0:5] == '◎译\u3000\u3000名':
            # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie['trans_name'] = each[6: len(each)]
            #print(movie["trans_name"])
        if each[0:5] == "◎年\u3000\u3000代":
            # ◎年　　代　2019 ,2019从第7位开始
            movie["decade"] = each[6: len(each)]
            print(movie["decade"])
        elif each[0:5] == "◎产\u3000\u3000地":
            movie["country"] = each[6: len(each)]
        elif each[0:5] == "◎类　　别":
        # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["type"] = each[6: len(each)]
        elif each[0:5] == "◎上映日期":
        # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["subtitles"] = each[6: len(each)]
        # ◎IMDb评分有7位
        elif each[0:7] == "◎IMDb评分":
        # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["IMDb_socre"] = each[9: len(each)]
        elif each[0:5] == "◎豆瓣评分":
        # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["douban_socre"] = each[6: len(each)]
        elif each[0:5] == "◎文件格式":
        # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["format"] = each[6: len(each)]
        elif each[0:5] == "◎视频尺寸":
        # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["resolution"] = each[6: len(each)]
        elif each[0:5] == "◎文件大小":
            # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["size"] = each[6: len(each)]
        elif each[0:5] == "◎片\u3000\u3000长":
            # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["duration"] = each[6: len(each)]
        elif each[0:5] == "◎导\u3000\u3000演":
            # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            movie["director"] = each[6: len(each)]
        elif each[0:5] == "◎主\u3000\u3000演":
            # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
            # 主演
            actor = each[6: len(each)]
        for item in content:
            if item[0: 4] == '\u3000\u3000\u3000\u3000':
                actor = actor + '\n' + item[6: len(item)]
        movie["actor"] = actor
        movie["ftp"] = html.xpath("//div[@class='co_content8']/ul/tr/td/div/td/table/tbody/tr/td/a/text()")
        return movie


def spider():
    base_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
    for i in range(1,8):
        url = base_url.format(i)
        detail_uels = get_detail_urls(url)
        for url1 in detail_uels:
            movie = parse_movie(url1)
            #print(movie)


if __name__ == '__main__':
    spider()