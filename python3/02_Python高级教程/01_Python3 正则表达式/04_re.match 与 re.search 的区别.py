'''
re.match 与 re.search 的区别
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None;
而 re.search 匹配整个字符串，直到找到一个匹配。
'''
import re

line = 'Cat are smarter than dogs';

matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print('match --> matchObj.group() : ', matchObj.group())
else:
    print('No match!!')

searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
    print('search --> searchObj.group() : ', searchObj.group())
else:
    print('No match!!')