# coding=utf-8

import urllib2

url = "http://www.baidu.com"
request = urllib2.Request(url)
request.get_method = lambda: "PUT"  # 或者 "DELETE"
response = urllib2.urlopen(request)

print response.read()
