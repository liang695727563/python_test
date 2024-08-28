'''
re.search 方法
re.search 扫描整个字符串并返回第一个成功的匹配。
函数语法：
re.search(pattern, string, flags=0)
函数参数说明：
参数            描述
pattern         匹配的正则表达式
string          要匹配的字符串。
flags           标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

匹配成功 re.seach() 方法返回一个匹配的对象，否则返回 None。
我们可以使用 group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法            描述
group(num=0)        匹配的整个表达式的字符串， group() 可以一次输入多个组号，
                    在这种情况下它将返回一个包含那些组所对应值的元组。
group()             返回一个包含所有小组字符串的元组，从 1 到 所含的小组号
'''
import re

print(re.search('www', 'www.w3cschool.cn').span())     # 在起始位置匹配
print(re.search('cn', 'www.w3cschool.cn').span())      # 不在起始位置匹配

print('-' * 30)

import re

line = 'Cats are smarter than dogs';

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print('searchObj-group() : ', searchObj.group())
    print('searchObj-group(1) : ', searchObj.group(1))
    print('searchObj-group(2) : ', searchObj.group(2))
else:
    print('Nothing found!!')