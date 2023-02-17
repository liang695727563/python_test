#coding=utf-8
# 正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。Python 自 1.5 版本起增加了 re 模块，它提供 Perl 风格的正则表达式模式。

# re 模块使 Python 语言拥有全部的正则表达式功能。

# compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。

# re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

import re

line = "Cate are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# 匹配成功 re.match 方法返回一个匹配的对象，否则返回 None。

# 我们可以使用 group(num) 或 groups() 匹配对象函数来获取匹配表达式。
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"

print '*' *30

# re.search 会在字符串内查找模式匹配，直到找到第一个匹配。
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print "searchObj.group() : ", searchObj.group()
    print "searchObj.group(1) : ", searchObj.group(1)
    print "searchObj.group(2) : ", searchObj.group(2)
else:
    print "Nothing found!!"

# re.match 与 re.search 的区别
# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None；而 re.search 匹配整个字符串，直到找到一个匹配。

