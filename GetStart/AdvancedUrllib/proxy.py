# coding=utf-8

import urllib2

# 设置代理服务器
proxies = {
    "http": "http://125.88.74.122:84"
}
proxy_handler = urllib2.ProxyHandler(proxies)
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

# 方法一：若 install opener 了
url = "http://www.baidu.com"
response = urllib2.urlopen(url)

# 方法二：若没有 install opener
# opener.open(url)

print response.read()
