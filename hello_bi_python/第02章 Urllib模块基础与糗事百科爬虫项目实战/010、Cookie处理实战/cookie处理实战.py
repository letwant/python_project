# Cookie经常用户会话控制，可以存储很多信息，常常用于反爬。
# 对Cookie的处理包括：
#1、Cookie的保存
#2、Cookie的读取
import urllib.request
import http.cookiejar
# 建立cookie处理
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener) # 将cookie变为全局，其他地方就可以使用cookie了

#cookie读取
print(str(cjar))