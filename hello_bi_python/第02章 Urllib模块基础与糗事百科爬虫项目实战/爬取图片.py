import re, urllib.request

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Connection": "keep-alive"
}
#创建opener对象
opener=urllib.request.build_opener()
headall = []
for key, value in headers.items():
    item = (key, value) #将字典中的元素保存为元组，然后存在一个list中
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
for i in range(20120, 20121):
    url = "https://www.ai768.com/tupian/" + str(i) +".html"
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    print(data)
    pat = 'data-original="(.*?)"'
    pic_url_list = re.compile(pat, re.S).findall(data)
    for pic_url in pic_url_list:
        print(pic_url)
        urllib.request.urlretrieve(pic_url, filename=r"E:\python_project\hellobi_Python爬虫教学\第二章 Urllib模块基础与糗事百科爬虫项目实战\图片")
