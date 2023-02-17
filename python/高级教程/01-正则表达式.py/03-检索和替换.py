#coding=utf-8
# Python 的 re 模块提供了 re.sub 用于替换字符串中的匹配项。

import re

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符中的 Python注解
num = re.sub( r'#.*$', "", phone)
print "电话号码是：", num

# 删除非数字（-）的字符串
num = re.sub( r'\D', "", phone)
print "电话号码是：", num

# re.sub(pattern, repl, string, max=0)
# 返回的字符串是在字符串中用 RE 最左边不重复的匹配来替换。如果模式没有发现，字符将被没有改变地返回。

# 可选参数 count 是模式匹配后替换的最大次数；count 必须是非负整数。缺省值是 0 表示替换所有的匹配。
# repl 参数是一个函数

# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print re.sub('(?P<value>\d+)', double, s)