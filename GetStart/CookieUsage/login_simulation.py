# coding=utf-8

import urllib
import urllib2
import cookielib

filename = "cookie.txt"
cookie_jar = cookielib.MozillaCookieJar(filename)
cookie_processor = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie_processor)

# 模拟登录
login_url = "http://sso.jwc.whut.edu.cn/Certification/login.do"
login_value = {
    "userName": "0121310880305",
    "password": "xxxxxxxxxxx",
    "type": "xs"
}
login_data = urllib.urlencode(login_value)
login_user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
login_request = urllib2.Request(login_url, login_data)
login_response = opener.open(login_request)
print login_response.geturl()
print login_response.getcode()
print login_response.info()
print login_response.read()

# 将 Cookie 存储到外部文件中
cookie_jar.save(filename, True, True)

# 使用 Cookie 访问需要登录的页面（此处有时会不返回 content，不知道为什么）
score_url = "http://202.114.90.180/Score/"
score_response = opener.open(score_url)
print score_response.geturl()
print score_response.getcode()
print score_response.info()
print score_response.read()
