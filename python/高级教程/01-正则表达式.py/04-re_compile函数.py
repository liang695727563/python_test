#coding=utf-8
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

import re

print 'began'

pattern = re.compile(r'\d+')                # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')    # 查找头部，没有匹配
print m             # None

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print m             # None

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print m             # 返回一个 Match 对象

m.group(0)          # 可省略 0
print m.group(0)

print m.start(0)    # 可省略 0

print m.end(0)      # 可省略 0

print m.span(0)     # 可省略 0 

print '*' * 30


import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello world Wide Web')
print m     # 匹配成功，返回一个 Match 对象

print m.group(0)    # 返回匹配成功的整个子串
print m.span(0)     # 返回匹配成功的整个子串的索引
print m.group(1)    # 返回第一个分组匹配成功的子串
print 'm.span(1):',m.span(1)     # 返回第一个分组匹配成功的子串的suoy
print m.group(2)    # 返回第二个分组匹配成功的子串
print m.span(2)     # 返回第二个分组匹配成功的子串
print m.groups()    # 等价于 (m.group(1), m.group(2),...)

print m.group(3)    # 不存在第三个fenzk
