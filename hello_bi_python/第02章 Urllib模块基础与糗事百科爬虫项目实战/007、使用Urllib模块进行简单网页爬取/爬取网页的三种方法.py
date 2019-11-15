import urllib.request
#爬到内存中的第一种方法: urlopen()
data = urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8", "ignore")
print(len(data))

#爬到内存中的第二种方法: Request() 一般POST方法会使用到
url = "http://www.baidu.com"
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
print(len(data))

#爬到硬盘中urllib.request.urlretrieve()
urllib.request.urlretrieve(url, filename=r"E:\python_project\hellobi_Python爬虫教学\第二章 Urllib模块基础与糗事百科爬虫项目实战\007、使用Urllib模块进行简单网页爬取\baidu.html")


# 拿到状态码 getcode()
file = urllib.request.urlopen("http://www.baidu.com")
print(file.getcode())