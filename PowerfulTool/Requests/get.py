# coding=utf-8

import requests
from PIL import Image
from io import BytesIO

# 传递 URL 参数
payload = {
    "key1": "value1",
    "key2": ["value2", "value3"]
}
# 定制请求头
headers = {
    "Content-Type": "application/json"
}
r = requests.get("http://httpbin.org/get", params=payload)

# Requests 会使用其推测的文本编码，可以通过 r.encoding 属性来改变它
r.encoding = "utf-8"

# 1. 解析响应内容
print r.text

# 2. 解析 JSON 响应内容
print r.json()

# 3. 解析二进制响应内容（图片、文件等）
r_binary = requests.get("http://httpbin.org/image", headers={"Accept": "image/jpeg"})
image = Image.open(BytesIO(r_binary.content))
print r_binary.content

# 4. 解析原始响应内容
r_raw = requests.get('https://github.com/timeline.json', stream=True)
print r_raw.raw.read()
