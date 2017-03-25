# coding=utf-8

import urllib2
import cookielib

cookie_jar = cookielib.MozillaCookieJar()
cookie_jar.load("cookie.txt", True, True)  # 加载文件中的 Cookie
cookie_processor = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie_processor)

response = opener.open("http://www.baidu.com")
print response.read()
