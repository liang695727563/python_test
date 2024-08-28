'''
另一个非常有用的 Python 内建数据类型是字典。

序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。

理解字典的最佳方式是把它看做无序的键 => 值对集合。在同一个字典之内，关键字必须是互不相同。

一对大括号创建一个空的字典：{}。
'''
tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))
print(sorted(tel.keys()))

print('guido' in tel)
print('jack' not in tel)

print('-' * 30)
# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# 此外，字典推导可以用来创建任意键和值的表达式词典：
print({x: x**2 for x in (2, 4, 6)})

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
print(dict(sape=4139, guido=4127, jack=4098))

