# coding=utf-8

import re

pattern = re.compile(r"world")

# 搜索满足 Pattern 的子串。与 match()不同，search()不需要只有在索引为 0 的位置匹配成功猜返回 MatchObject
result = re.search(pattern, "Hello world!")
if result:
    print result.group()
