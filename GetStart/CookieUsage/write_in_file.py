# coding=utf-8

import urllib2
import cookielib

filename = "cookie.txt"  # 声明文件名，位于当前目录
cookie_jar = cookielib.MozillaCookieJar(filename)  # 创建 FileCookieJar 或者其子类 MozillaCookieJar
cookie_processor = urllib2.HTTPCookieProcessor(cookie_jar)  # 创建 Cookie 处理器
opener = urllib2.build_opener(cookie_processor)  # 构建拥有 Cookie 处理能力的 Opener

response = opener.open("http://www.baidu.com")
cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 写入文件，丢弃和过期的 Cookie 依然保存
