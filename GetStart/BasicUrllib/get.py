# coding=utf-8

import urllib
import urllib2

values = {
    "type": "content",
    "q": "爬虫"
}

data = urllib.urlencode(values)
url = "https://www.zhihu.com/search"
complete_url = url + "?" + data
request = urllib2.Request(complete_url)
response = urllib2.urlopen(request)

print response.read()
