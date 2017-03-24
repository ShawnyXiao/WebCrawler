# coding=utf-8

import urllib2

# 开启调试日志
http_handler = urllib2.HTTPHandler(debuglevel=1)
https_handler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(http_handler, https_handler)
urllib2.install_opener(opener)

url = "http://www.baidu.com"
response = urllib2.urlopen(url)
