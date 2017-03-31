# coding=utf-8

import requests

# 发送各种类型的请求
r = requests.get('https://github.com/timeline.json')
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

print r.status_code
print r.encoding
print r.text
print r.cookies
