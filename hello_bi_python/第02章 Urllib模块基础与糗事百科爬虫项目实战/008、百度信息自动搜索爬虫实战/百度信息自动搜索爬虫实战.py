import urllib.request
import re
import json
url = "http://www.baidu.com/s?wd="
key = "电脑主机"
#对关键词进行编码，因为URL中需要对中文等进行处理

key_code = urllib.request.quote(key)

url_key = url + key_code + "&ie=utf-8"
pat = "data-tools='(.*?)'><a"
# 视频教程中的pat为 pat='"title":"(.*?)"'
file_path = r"E:\python_project\hellobi_Python爬虫教学\第二章 Urllib模块基础与糗事百科爬虫项目实战\百度信息爬取结果.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("----------------------------结果----------------------------\n")
with open(file_path, "a", encoding="utf-8") as f1:
    for i in range(10):
        work_url = url_key + "&pn=" + str(i)
        res_html = urllib.request.urlopen(work_url).read().decode("utf-8", "ignore")
        info_list = re.compile(pat, re.S).findall(res_html)
        for item in info_list:
            info = json.loads(item)
            f1.write("标题: " + info["title"] + "\n")
            f1.write("地址: " + info["url"] + "\n")

            f1.write("-----------------------------------------------------------------\n")