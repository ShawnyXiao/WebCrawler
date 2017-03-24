# coding=utf-8

import urllib2

request = urllib2.Request("http://blog.csdn.net/cqcre")
try:
    urllib2.urlopen(request)
except urllib2.HTTPError, e:  # 子类异常在前
    print e.code
except urllib2.URLError, e:  # 父类异常在后
    if hasattr(e, "reason"):  # 对异常属性进行判断
        print e.reason
else:
    print "OK"
