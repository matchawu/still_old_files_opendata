#!/usr/bin/python3
import requests
import json

# Python 字典类型转换为 JSON 对象
# data1 = {
#     'no' : 1,
#     'name' : 'w3big',
#     'url' : 'http://www.w3big.com'
# }

data1 = requests.get("http://opendata2.epa.gov.tw/AQI.json")

json_str = json.dumps(data1.text)
# print ("Python 原始数据：", repr(data1))
# print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print (data2{"url"})
# print ("data2['url']: ", data2['url'])