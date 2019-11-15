# 淘宝商品图片爬虫
import urllib.request
import re
keyname = "连衣裙"
key = urllib.request.quote(keyname)
if __name__ == '__main__':

    for i in range(1, 101):
        url = "https://s.taobao.com/search?q=" + key + "&s=" + str((i-1) * 44)
        source_html = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        pat = '"pir_url":"//(.*?)"'
        img_list = re.compile(pat).findall(source_html)
        for img in img_list:
            work_url = "http://" + img
            local_file = "E:/python_project/hellobi_Python爬虫教学/第03章 淘宝商品图片爬虫开发实战/018、编写淘宝商品图片爬虫实战/淘宝图片/" + img + ".jpg"
            urllib.request.urlretrieve(img, filename=local_file)