import requests

# 运行get请求
r = requests.get('https://api.github.com/events')
print(r.headers)

r = requests.post('https://httpbin.org/post', data = {'key':'value'})