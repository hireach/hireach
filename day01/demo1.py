from urllib import request

#加请求头就可以了
opener = request.build_opener()
opener.addheaders = [( 'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')]
request.install_opener(opener)

request.urlretrieve("http://img.doutula.com/production/uploads/image//2019/05/06/20190506145263_nBPAyj.png",'Ni')