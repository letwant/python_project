# IP代理池中的IP不一定是有效IP，有时需要我们对代理IP进行自动过滤与筛选
import time
import urllib.request

# ippools是标志位， myurl是要爬的地址，thisapi是接口的地址
def use_ip(ippools, myurl, thisapi):
    def api(thisapi):
        import urllib.request
        print("这一次调用了接口")
        import urllib.request
        urllib.request.urlcleanup()
        thisall = urllib.request.urlopen(thisapi).read().decode("utf-8", "ignore")
        print("接口调用完成")
        return thisall
    # 将得到的IP添加到请求头中
    def ip(ippools):
        thisip = ippools
        print("当前用的IP是: {}".format(ippools))
        proxy = urllib.request.ProxyHandler({"http":thisip})
        opener = urllib.request.build_opener(opener)
    if(ippools == 0):
        while True:
            ippools = api(thisapi)
            print("提取IP完成")
            ip(ippools)
            print("正在验证IP有效性")
            data1 = urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8", "ignore")
            if(len(data1) > 5000):
                print("-------当前IP有效--------")
                break
            else:
                print("-------当前IP无效--------")
                time.sleep(60)
    else:
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
        # 第一次
        if(i % 7 == 0 and i == 0):
            ippools, thispagedata = use_ip(0, url, thisapi)
        # 第七次，切换ip
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