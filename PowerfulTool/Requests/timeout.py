# coding=utf-8

import requests

# 为防止服务器不能及时响应，大部分发至外部服务器的请求都应该带着 timeout 参数
url = "http://www.baidu.com"
r = requests.get(url, timeout=1)
print r.text
