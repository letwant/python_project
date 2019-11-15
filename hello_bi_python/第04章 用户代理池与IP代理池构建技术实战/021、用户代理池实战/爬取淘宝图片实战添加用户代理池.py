# 添加用户代理池
import urllib.request
import re
import random
keyname = "连衣裙"
key = urllib.request.quote(keyname)
uapools = [
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
]

def ua(uapools):
    thisua = random.choice(uapools)
    headers = ("User-Agent", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 安装为全局
    urllib.request.install_opener(opener)

for i in range(1, 101):
    try:
        print('------------正在爬取第{}页------------'.format(i))
        url = "https://s.taobao.com/search?q=" + key + "&s=" + str((i-1) * 44)
        ua(uapools)
        source_html = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        pat = '"pir_url":"//(.*?)"'
        img_list = re.compile(pat).findall(source_html)
        for img in img_list:
            try:
                work_url = "http://" + img
                local_file = "E:/python_project/hellobi_Python爬虫教学/第03章 淘宝商品图片爬虫开发实战/018、编写淘宝商品图片爬虫实战/淘宝图片/" + img + ".jpg"
                urllib.request.urlretrieve(img, filename=local_file)
            except Exception as err:
                pass
    except Exception as err:
        pass