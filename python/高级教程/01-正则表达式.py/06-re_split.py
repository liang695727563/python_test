#coding=utf-8
# split 方法按照能够匹配的子串将字符串分割后返回列表

import re

print re.split('\W+', 'w3cschool, w3cschool,w3cschool.')
print re.split('(\W+)',' w3cschool,w3cschool,w3cschool.')
print re.split('\W+',' w3cschool, w3cschool,w3cschool.', 1)

print re.split('a*', 'hello world')     # 对于一个找不到匹配的字符串而言，split 不会对其做出分割
