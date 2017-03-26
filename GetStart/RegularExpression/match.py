# coding=utf-8

import re

# 将正则表达式编译成 Pattern
pattern = re.compile(r"hello")  # r 表示原生字符串，不转义

# 使用 Pattern 匹配字符串，匹配成功将返回 MatchObject，匹配失败将返回 None
result1 = re.match(pattern, "hello")
result2 = re.match(pattern, "helloo hello world")
result3 = re.match(pattern, "helo world")
result4 = re.match(pattern, "hello world")

if result1:
    print result1.group()  # 打印 MatchObject 中的所有分组
else:
    print "匹配 1 失败！"

if result2:
    print result2.group()
else:
    print "匹配 2 失败！"

if result3:
    print result3.group()
else:
    print "匹配 3 失败！"

if result4:
    print result4.group()
else:
    print "匹配 4 失败！"
