# coding=utf-8

import re


def title(m):
    return m.group(1).title() + " " + m.group(2).title()


pattern = re.compile(r"(\w+) (\w+)")
text = "i say, hello world!"

# 将分组 2 与分组 1 进行调换，并返回替换次数
print re.subn(pattern, r"\2 \1", text)

# 将分组 1 和分组 2 的首字母都大写，并返回替换次数
print re.subn(pattern, title, text)
