# coding=utf-8

import urllib2

# 方法一：直接访问 URL
# response = urllib2.urlopen("http://www.baidu.com")

# 方法二：构建请求，访问 URL
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)

print response.read()
