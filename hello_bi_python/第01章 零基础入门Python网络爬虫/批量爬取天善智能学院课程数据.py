import urllib.request
import re

data = urllib.request.urlopen("https://edu.hellobi.com/course/211").read().decode("utf-8", "ignore")
print(len(data))
part = "<title>(.*?)</title>"
res = re.compile(part, re.S).findall(data)
print(res)

# 正式代码
path = r"E:\python_project\hellobi_Python爬虫教学\第一章 零基础入门Python网络爬虫\info.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("------------授课信息------------\n")
with open(path, "a", encoding="utf-8") as f1:
    for i in range(1, 50):
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
        f1.write("课程名: " + title + "\n")
        f1.write("授课老师: " + teacher + "\n")
        f1.write("课程价格:" + price + "\n")
        f1.write("------------------\n")
