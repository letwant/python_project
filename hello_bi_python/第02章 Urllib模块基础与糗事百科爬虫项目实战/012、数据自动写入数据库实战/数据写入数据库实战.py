import urllib.request
import re
import pymysql # 将虚拟环境中的site-package的pymysql中的connect.py文件中charset默认为空改为"utf8"，不要加"-"
conn = pymysql.connect(host='192.168.3.40', user='root', passwd='root', db='app')
# 正式代码
path = r"E:\python_project\hellobi_Python爬虫教学\第一章 零基础入门Python网络爬虫\info.txt"
for i in range(1, 20):
    this_url = "https://edu.hellobi.com/course/" + str(i)
    data = urllib.request.urlopen(this_url).read().decode("utf-8", "ignore")
    title_pat = '<li class="active">(.*?)</li>'
    teacher_pat = 'class="lec-name">(.*?)<'
    price_pat = 'div class="course-price">.*?<sub>￥</sub>(.*?)<'
    title = re.compile(title_pat, re.S).findall(data)
    if (len(title) > 0):
        title = title[0]
    else:
        continue
    teacher = re.compile(teacher_pat, re.S).findall(data)
    if (len(teacher) > 0):
        teacher = teacher[0]
    else:
        continue
    price = re.compile(price_pat, re.S).findall(data)
    if (len(price) > 0):
        price = price[0]
    else:
        price = "免费"
    conn.query("INSERT INTO lesson(title, teacher, price) VALUES('"+str(title)+"', '"+str(teacher)+"', '"+str(price)+"')")
    conn.commit()