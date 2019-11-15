# beautifulSoup也可以实现信息的筛选和提取
from bs4 import BeautifulSoup as bs
import urllib.request
data = urllib.request.urlopen("http://edu.iqianyue.com/").read().decode("utf-8", "ignore")
bs1 = bs(data)
#格式化输出
#print(bs1.prettify())
#获取标签: bs对象.标签名.string
title = bs1.title
#获取标签里面的文字: bs对象.标签名.name
str = bs1.a.name
#获取属性列表: bs对象.标签名.attrs
attrs = bs1.a.attrs
#获取某个属性对应的值: bs对象.标签名[属性名] 或者bs对象.标签名.get(属性名)
clas = bs1.a["class"]
cla = bs1.a.get("class")