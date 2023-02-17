#coding=utf-8
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： motch 和 search 是匹配一次 findall 匹配所有

import re;

pattern = re.compile(r'\d+')    # 查找数字
result1 = pattern.findall('school 123 google 456')
result2 = pattern.findall('sch88ool123gogle456', 0, 10)

print result1
print result2

print '*'*30

# re.finditer
# 和findall类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

import re

it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print match.group()