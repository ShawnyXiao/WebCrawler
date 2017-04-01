# coding=utf-8

import requests
import json

# 传递编码为表单形式的数据
form_payload = {
    "key1": "value1",
    "key2": "value2"
}
r_form = requests.post("http://httpbin.org/post", data=form_payload)
print r_form.text

# 传递编码为 JSON 的数据
json_payload = {
    "a": True,
    "b": "Hello",
    "c": None
}
r_json = requests.post("http://httpbin.org/post", data=json.dumps(json_payload))  # 方法一：对 dict 进行编码
# r_json = requests.post("http://httpbin.org/post", json=json_payload)  # 方法二：直接使用 json 参数传递，会被自动编码
print r_json.text

# 传递多部分编码（Multipart-Encoded）的文件
files = {
    "file": open("post.txt", "rb")
}
r_file = requests.post("http://httpbin.org/post", files=files)
# with open("post.txt") as f:  # Requests 支持流式上传，这允许你发送大的数据流或文件而无需先把它们读入内存
#     r_file = requests.post("http://httpbin.org/post", data=f)
print r_file.text
