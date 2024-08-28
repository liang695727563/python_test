# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:

import fibo, sys

print(dir(fibo))

print(dir(sys))

print()
print('-' * 30)
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
print(dir())  # 得到一个当前模块中定义的属性列表

a = 5   # 建立一个新的变量 'a'
print(dir())

del a   # 删除变量名称a
print(dir())
