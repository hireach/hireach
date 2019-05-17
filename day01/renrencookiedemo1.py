import requests

url2 = "http://www.renren.com/880151247/profile"
url = "http://www.renren.com/PLogin.do"
data = {
    "email":"970138074@qq.com",
    "password":"pythonspider"
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

session = requests.session()
session.post(url,data=data,headers=headers)
response = session.get(url2)
print(response.content.decode('utf-8'))