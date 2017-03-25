# coding=utf-8

import urllib2
import cookielib

cookie_jar = cookielib.CookieJar()  # 创建一个 CookieJar
cookie_processor = urllib2.HTTPCookieProcessor(cookie_jar)  # 创建 Cookie 处理器
opener = urllib2.build_opener(cookie_processor)  # 构建拥有处理 Cookie 功能的 Opener

response = opener.open("http://www.baidu.com")
for item in cookie_jar:
    print item.name + " : " + item.value  # 输出 Cookie 中的键值对
