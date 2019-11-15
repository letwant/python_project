# IP代理池构建的第一种方案（适合于代理IP稳定的情况）
import urllib.request
import re
import random
ippools = [
    "114.230.106.216:31912",
    "49.85.12.116:30348",
    "127.0.0.1:8888",
]
def ip(ippools):
    thisip = random.choice(ippools)
    proxy = urllib.request.ProxyHandler({"http":thisip})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    # 安装为全局
    urllib.request.install_opener(opener)
keyname = "连衣裙"
key = urllib.request.quote(keyname)
for i in range(1, 101):
    try:
        ip(ippools)
        print('------------正在爬取第{}页------------'.format(i))
        url = "https://s.taobao.com/search?q=" + key + "&s=" + str((i-1) * 44)
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