# coding=utf-8

import requests

# 获取 Cookies
url_get = "http://www.baidu.com"
r_get = requests.get(url_get)
print r_get.cookies

# 设置 Cookies
url_set = "http://httpbin.org/cookies"
cookies_set = {
    "session_id": "fake"
}
r = requests.get(url_set, cookies=cookies_set)
print r.text
