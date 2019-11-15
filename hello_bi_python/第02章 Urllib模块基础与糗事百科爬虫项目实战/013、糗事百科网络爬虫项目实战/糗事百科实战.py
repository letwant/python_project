# 要加一个浏览器模拟
import urllib.request
import re

source_url = 'https://www.qiushibaike.com/8hr/page/'
file_path = r'E:\python_project\hellobi_Python爬虫教学\第二章 Urllib模块基础与糗事百科爬虫项目实战\013、糗事百科网络爬虫项目实战\段子.txt'
pat = '<div class="content">.*?<span>(.*?)</span>'
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]  # 将header添加到request中
urllib.request.install_opener(opener) # 或者将opener对象安装为全局变量，这样其他地方就可以访问了
with open(file_path, "a", encoding="utf-8") as f: # 字节编码不能少
    for i in range(1, 4):
        try:
            work_url = source_url + str(i) + '/'
            source_html = urllib.request.urlopen(work_url).read().decode('utf-8', 'ignore')
            joke_list = re.compile(pat, re.S).findall(source_html + '\n')
            for joke in joke_list:
                joke = joke.replace('<br>', '\n')
                joke = joke.replace('<br/>', '\n')
                f.write(joke)
                f.write('---------------------------------------------------------------------------\n')
        except Exception as e:
            pass