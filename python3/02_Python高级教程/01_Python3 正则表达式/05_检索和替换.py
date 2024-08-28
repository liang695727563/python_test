'''
检索和替换
Python 的 re 模块提供了 re.sub 用于替换字符串中的匹配项。
语法：
re.sub(pattern, rep1, string, max=0)
返回的字符串是在字符串中用 re 最左边不重复的匹配来替换。如果模式没有发现，字符将被没有改变地返回。
可选参数 count 是模式匹配后替换的最大次数；count 必须是非负整数。缺省值是 0 表示替换所有的匹配。
'''
import re

phone = '2004-959-559 # 这是一个电话号码'

# 删除注释
num = re.sub(r'#.*$', "", phone)
print('电话号码：', num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print('电话号码：', num)