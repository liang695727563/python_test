# coding=utf-8
import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
jsonString = json.dumps(data)  # json.dumps 用于将 Python 对象编码成 JSON 字符串。
print jsonString

import json

# 使用参数让 JSON 数据格式化输出：
print json.dumps({'a': 'W3Cschool', 'b': 7}, sort_keys=True, indent=4, separators=(',', ':'))

import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = json.loads(jsonData)  # json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
print text

# json 类型转换到 Python 的类型对照表：
# JSON	        Python
# object	    dict
# array	        list
# string	    unicode
# number (int)	int, long
# number (real)	float
# true	        True
# false	        False
# null	        None

print '*' * 50
# Demjson 是 python 的第三方模块库，可用于编码和解码 JSON 数据，包含了 JSONLint 的格式化及校验功能。
import demjson

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
jsonStr = demjson.encode(data)
print jsonStr

jsonStr = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = demjson.decode(jsonStr)
print text
