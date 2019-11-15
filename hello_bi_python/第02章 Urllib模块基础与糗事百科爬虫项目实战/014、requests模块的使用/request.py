# requests模块也是爬虫的常用模块 , 注意与request的区分
import requests
import re
'''
请求方式: get,post, put...
参数: params、headers、proxies、cookies、data
'''

rsp = requests.get("https://www.hellobi.com/")
print(rsp)

# 打印网页源代码
data = rsp.text
print(len(data))
#打印网页二进制源代码
data = rsp.content
print(len(data))
# 查看网页的url
print(rsp.url)
#查看网页的编码
print(rsp.encoding)
#查看网页的cookies
print(rsp.cookies)
#将cookie转为字典格式
data = requests.utils.dict_from_cookiejar(rsp.cookies)
print(data)
#查看网页的状态码
print(rsp.status_code)

title = re.compile("<title>(.*?)</title>", re.S).findall(rsp.text)

# 添加请求头，结构为字典格式
heads = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
cookies = rsp.cookies
proxy = {"http": "http://127.0.0.1:8888",
         "https": "https://127.0.0.1:8888"}
res = requests.get("https://www.hellobi.com/", heads=heads, cookies=cookies)

key={"wd": "letwant"}
rsp=requests.get("https://www.baidu.com/s", heads=heads, cookies=cookies, params=key)
title = re.compile("<title>(.*?)</title>", re.S).findall(rsp.text)
print(title)

# post请求 post数据
post_data = {
    "name": "letwant",
    "passwd": "abc123"
}
rsp = requests.post("http://www.iqianyue.com/mypost/", data=post_data)
print(rsp)
