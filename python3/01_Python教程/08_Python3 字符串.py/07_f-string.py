'''f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。

之前我们习惯用百分号 (%):
'''
name = 'W3Cschool'
print('Hello %s' % name)

# f-string 格式化字符串以 f 开头，后面跟着字符串，
# 字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去

name = 'W3Cschool'
print(f'Hello {name}')  # 替换变量

print(f'{1+2}')         # 使用表达式

w = {'name': 'W3Cschool', 'url': 'www.w3cschool.cn'}
print(f'{w["name"]}: {w["url"]}')

'''用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。

在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果：
'''
x = 1
print(f'{x+1}')   # Python 3.6

x = 1
print(f'{x+1=}')   # Python 3.8

'''
Unicode 字符串
在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。

在Python3中，所有的字符串都是Unicode字符串。
'''