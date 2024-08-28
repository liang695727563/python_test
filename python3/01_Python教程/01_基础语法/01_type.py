# Python 保留字
import keyword

print(keyword.kwlist)

# Python 中单行注释以 # 开头，多行注释采用三对单引号（'''）或者三对双引号（"""）将注释括起来。

#这是单行注释

"""
这是多行注释
这是多行注释
"""
'''
也可以用三个单引号来进行多行注释
'''


'''
类型判断
python可以用type函数来检查一个变量的类型，使用方法如下：
'''
x = 'W3cschool'
print(type(x))
x = 100
print(type(x))
x = (1,2,3)
print(type(x))
x = ['1','2','3']
print(type(x))