# coding=utf-8

import urllib
import urllib2

# 方法一：直接初始化字典类型的变量
# values = {
#     "email": "772077730@qq.com",
#     "password": "hn*******"
# }

# 方法二：声明后，通过 key 放入 key-value 对
values = {}
values["email"] = "772077730@qq.com"
values["password"] = "hn*******"

data = urllib.urlencode(values)
url = "https://www.zhihu.com/login/email"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)

print response.info()
print response.read()

