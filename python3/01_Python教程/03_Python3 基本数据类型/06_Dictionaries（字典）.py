'''
字典（dictionary）是 Python 中另一个非常有用的内置数据类型。

字典是一种映射类型（mapping type），它是一个无序的键值对（key-value）集合。

关键字（key）必须使用不可变类型，也就是说list和包含可变类型的 tuple 不能做关键字。

在同一个字典中，关键字（key）必须互不相同。
'''

dic = {} # 创建空字典
tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
print(tel)
print(tel['Jack']) # 主要的操作：通过key查询

del tel['Rose'] # 删除一个键值对
tel['Mary'] = 4175 # 添加一个键值对
print(tel)

print(list(tel.keys())) # 返回所有key组成的list

print(list(tel.values())) # 返回所有 value 组成的list

print(sorted(tel.keys())) # 按key排序
print(tel)

print('Tom' in tel) # 成员测试
print('Mary' not in tel) # 成员测试

print('+' * 30)

 
# 构造函数 dict() 直接从键值对 sequence 中构建字典，当然也可以进行推导
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print({x: x**2 for x in (2, 4, 6)})

print(dict(sape=4139, guido=4127, jack=4098))

'''
另外，字典类型也有一些内置的函数，例如 clear()、keys()、values() 等。

注意：

1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
'''