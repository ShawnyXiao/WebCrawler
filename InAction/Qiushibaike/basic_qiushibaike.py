# coding=utf-8

import urllib2
import re
import time

# 设置请求 URL
total_page = 35
url_without_page = "http://www.qiushibaike.com/8hr/page/"

# 设置请求头
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {
    "User-Agent": user_agent,  # 伪装成浏览器
    "Referer": "http://www.qiushibaike.com"  # 对付“防盗链”
}

try:
    # 获取 HTML 文档
    documents = ""
    for i in range(1, total_page + 1):
        request = urllib2.Request(url_without_page + str(i), headers=headers)  # 创建请求

        time.sleep(0.5)  # 暂停 0.5 秒，确保相应正常返回
        response = urllib2.urlopen(request)  # 发出请求

        documents += response.read().decode("utf-8")  # 获取整个 HTML 文档并合并成一个超长文本

    # 编译 Pattern
    pattern = re.compile(r'<div.*?author.*?<h2>(.*?)</h2>.*?<div.*?content.*?<span>(.*?)</span>(.*?)stats.*?<i.*?number">(.*?)</i>.*?<span.*?stats-comments.*?<i.*?number">(.*?)</i>', re.DOTALL)

    # 查找所有满足 Pattern 的子串
    results = re.findall(pattern, documents)

    # 将结果输出到控制台
    for m in results:
        have_img = re.search(r"img", m[2])  # 过滤掉带图片的段子
        if not have_img:
            print m[0] + u"：\n" + m[1] + u"\n（收获 " + m[3] + u" 个赞和 " + m[4] + u" 个评论）\n"
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
