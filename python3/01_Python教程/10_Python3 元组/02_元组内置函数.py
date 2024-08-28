'''
元组内置函数
'''

tuple1 = ('Google', 'W3CSchool', 'Taobao')
print(len(tuple1))      # 	len(tuple) 计算元组元素个数。

tuple2 = ('5', '4', '8')
print(max(tuple2))      # 	max(tuple) 返回元组中元素最大值。
print(max(tuple2))      #   min(tuple) 返回元组中元素最小值。

list1= ['Google', 'Taobao', 'W3CSchool', 'Baidu']
tuple1=tuple(list1)     #   tuple(seq) 将列表转换为元组。
print(tuple1)
print(type(tuple1))


import operator
dict1 = (1, 2, 3)
dict2 = ('a', 'b', 'c')
print(operator.eq(dict1, dict2))  # 	operator(tuple1,tuple2)  比较两个元组元素

print('*' * 30)
'''
关于元组是不可变的
所谓元组的不可变指的是元组所指向的内存中的内容不可变。
'''
tup = ('W', '3', 'C', 's', 'c', 'h','o','o','l')
# tup[0] = 'w'     # 不支持修改元素

print(id(tup))     # 查看内存地址
tup = (1,2,3)
print(id(tup))     # 查看内存地址, 内存地址不一样了
'''
从以上实例可以看出，重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象。
'''
