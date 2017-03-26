# coding=utf-8

import re

pattern = re.compile(r"\d+")

# 使用 Pattern 分割字符串
result = re.split(pattern, "Hello58796world56456!")
print result
