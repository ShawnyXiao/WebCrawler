# coding=utf-8

import urllib
import urllib2

url = "https://www.zhihu.com/login/email"

values = {
    "email": "772077730@qq.com",
    "password": "hn*******"
}
data = urllib.urlencode(values)

# 设置请求头
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {
    "User-Agent": user_agent,  # 伪装成浏览器
    "Referer": url  # 对付“防盗链”
}

request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)

print response.info()
print response.read()
