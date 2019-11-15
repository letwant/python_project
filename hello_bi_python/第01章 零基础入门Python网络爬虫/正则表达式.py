import re


# 格式 re.compile(正则表达式).findall(源字符串)
def output(pat, source_str):
    data = re.compile(pat, re.S).findall(source_str)
    print(data)


pat, source = "ABC", "baiduABCjhskjalskdjf"
output(pat, source)

source = '''aliyun
edu'''
pat = "yun\n"
output(pat, source)

source = "aliyu89787nedu"
pat = "\w\d\w\d\d\w"
output(pat, source)

pat = "\w\d[nedu]\w"
output(pat, source)