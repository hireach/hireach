import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts


ALL_DATA =[]


def parse_page(url,num):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    if num == 1:
        soup = BeautifulSoup(text,"lxml")
    else:
        soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find("div",class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            lowest_temp = tds[-2]
            lowest_temp = list(lowest_temp.stripped_strings)[0]
            ALL_DATA.append({"city":city,"lowest_temp":int(lowest_temp)})

def main():
    urls = {
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml"
    }
    for url in urls:
        if url == "http://www.weather.com.cn/textFC/gat.shtml":
            parse_page(url,2)
        else:
            parse_page(url,1)
    # 分析数据
    ALL_DATA.sort(key=lambda data:data["lowest_temp"])
    data = ALL_DATA[0:10]
    citys = list(map(lambda x:x["city"],data))
    temp = map(lambda x:x["lowest_temp"],data)
    bar = (
        Bar()
            .add_xaxis(citys)
            .add_yaxis("最低温度",list(temp))
            .set_global_opts(title_opts=opts.TitleOpts(title="中国近三天温度排行"))
    )
    bar.render('temp.html')


if __name__ == '__main__':
    main()