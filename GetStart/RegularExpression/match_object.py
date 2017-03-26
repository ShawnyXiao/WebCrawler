# coding=utf-8

import re

pattern = re.compile(r"(\w+) (\w+)(?P<sign>.*)")  # (?P<name>...)：为分组指定一个别名

result = re.match(pattern, "Hello world!")

print "result.string: ", result.string  # 匹配使用的字符串
print "result.re: ", result.re  # 匹配使用的 Pattern 对象
print "result.pos: ", result.pos  # 在字符串中，匹配的起始索引
print "result.endpos: ", result.endpos  # 在字符串中，匹配的结束索引
print "result.lastindex: ", result.lastindex  # 最后一个被捕获的分组的编号
print "result.lastgroup: ", result.lastgroup  # 最后一个被捕获的分组的别名
print "result.group(): ", result.group()  # 所有被捕获的分组组成的字符串
print "result.group(1, 2): ", result.group(1, 2)  # 被捕获的第 1 和第 2 个分组组成的 tuple
print "result.groups(): ", result.groups()  # 所有被捕获的分组组成的 tuple
print "result.groupdict(): ", result.groupdict()  # 有别名的分组的别名为键、以该分组截获的子串为值的字典
print "result.start(2): ", result.start(2)  # 被捕获的第 2 个分组在字符串中的起始索引
print "result.end(2): ", result.end(2)  # 被捕获的第 2 个分组在字符串中的结束索引
print "result.span(2): ", result.span(2)  # (start(2), end(2))
print r"result.expand(r'\g<2> \1\g<sign>') :", result.expand(r"\g<2> \1\g<sign>")  # # 捕获到的分组代入 template 中
