# 有时候经常需要将爬虫模拟成浏览器，有三种方式实现：
#1、通过Openner添加headers
#2、通过Request添加headers
#3、批量添加headers

#例如，如果不伪装成浏览器爬取糗事百科，会被远程拒绝
import urllib.request
data = urllib.request.urlopen("https://www.qiushibaike.com/").read() # 缺少User-Agent字段