import urllib.request

url = "https://www.qiushibaike.com/"
# 头文件格式header=("User-Agent", 具体用户代理值)
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]  # 将header添加到request中
data = opener.open(url).read() # 已经完成浏览器伪装，可以对url进行访问
urllib.request.install_opener(opener) # 或者将opener对象安装为全局变量，这样其他地方就可以访问了
data = urllib.request.urlopen(url).read()


# 第二种要添加多个头部信息
 # 先用字典保存
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Referer":"https://www.qiushibaike.com/",
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
data = urllib.request.urlopen(url).read()


# 第三种是使用request模块去模拟浏览器
req = urllib.request.Request(url)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
res_data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')