# IP代理池实现的第二种方式（接口调用法，这种方法更适合于代理IP不稳定的情况）
import time
import urllib.request

def use_ip(ippools, myurl, thisapi):
    def api(thisapi):
        import urllib.request
        print("这一次调用了接口")
        import urllib.request
        urllib.request.urlcleanup()
        thisall = urllib.request.urlopen(thisapi).read().decode("utf-8", "ignore")
        print("接口调用完成")
        return thisall

    def ip(ippools):
        thisip = ippools
        print("当前用的IP是: {}".format(ippools))
        proxy = urllib.request.ProxyHandler({"http":thisip})
        opener = urllib.request.build_opener(opener)
    if(ippools == 0):
        ippools = api(thisapi)
        print("提取IP完成")
    ip(ippools)
    url = myurl
    data1 = urllib.request.urlopen(url).read()
    data = data1.decode("gbk", "ignore")
    return ippools, data
x = 0
thisapi = ''
for i in range(0, 35):
    try:
        url = "http://www.baidu.com"
        if(i % 7 == 0 and i == 0):
            ippools, thispagedata = use_ip(0, url, thisapi)
        elif(i % 7 == 0):
            print("正在延时中...")
            time.sleep(15)
            print("延时完成，正在调取IP")
            ippool, thispagedata = use_ip(0, url, thisapi)
            print("IP调取完成")
        else:
            ippools, thispagedata = use_ip(0, url, thisapi)
        print(len(thispagedata))
        x += 1
    except Exception as err:
        print(err)
        x +=1