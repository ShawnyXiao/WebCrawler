# coding=utf-8

import re

pattern = re.compile(r"\d+")

# 找出所有符合 Pattern 的子串，组成一个列表
result = re.findall(pattern, "Hello896464world4564564!")
print result
