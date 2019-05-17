import requests

url = 'https://www.httpbin.org/ip'

# 代理
proxy = {"http":"183.166.124.1:13300",}

response = requests.get(url,proxies=proxy)
print(response.content)