# coding=utf-8

import re

pattern = re.compile(r"\w+ly")
text = "He was carefully disguised but captured quickly by police."

# finditer()返回一个可迭代的容器，其中装载的对象是 MatchObject
for m in re.finditer(pattern, text):
    print '%02d-%02d: %s' % (m.start(), m.end(), m.group())
