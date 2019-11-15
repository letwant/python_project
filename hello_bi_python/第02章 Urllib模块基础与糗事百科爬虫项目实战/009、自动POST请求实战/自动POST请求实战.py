# 自动POST爬虫

import urllib.request
import urllib.parse

url = 'http://www.iqianyue.com/mypost'
post_data = urllib.parse.urlencode({ # post上传的表单
    "name": "ceo@iqianyue.com",
    "pass": "aA123456"
}).encode('utf-8') # 将数据使用urlencode编码处理后，使用encode()设置为utf-8编码
req = urllib.request.Request(url, post_data)
req.add_header('User-Agent' ,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
res_data = urllib.request.urlopen(req).read()
with open(r"E:\python_project\hellobi_Python爬虫教学\第二章 Urllib模块基础与糗事百科爬虫项目实战\009、自动POST请求实战\posttest.html", "wb") as fhandle:
    fhandle.write(res_data)
