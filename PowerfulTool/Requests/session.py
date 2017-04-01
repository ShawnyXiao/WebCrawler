# coding=utf-8

import requests

# 创建 Session 对象
s = requests.Session()

# 为请求方法提供缺省数据
s.auth = ("user", "pass")
s.headers.update({
    "x-test": "true"
})

# 若想要舍弃缺省数据，对应字段设置为 None
# s.headers.update({
#     "x-test": None
# })

# 在会话中，跨请求保持 Cookie
s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
r = s.get("http://httpbin.org/get", headers={"xx-test": "false", "x-test": "false"})  # 方法级别的参数不会在会话中保持，且可以覆盖缺省参数
print r.text
r = s.get("http://httpbin.org/get")
print r.text
