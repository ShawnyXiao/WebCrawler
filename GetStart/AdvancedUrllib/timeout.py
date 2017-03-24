# coding=utf-8

import  urllib
import urllib2

url = "http://www.baidu.com"

# 方法一：若没有 data 传入
# response = urllib2.urlopen(url, timeout=10)

# 方法二：若有 data 传入
values = {
    "Referer": url
}
data = urllib.urlencode(values)
response = urllib2.urlopen(url, data, 10)

print response.read()
