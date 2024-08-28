'''
集合（set）是一个无序的不重复元素序列。因此在每次运行的时候集合的运行结果的内容都是相同的，但元素的排列顺序却不是固定的，所以本章中部分案例的运行结果会出现与给出结果不同的情况（运行结果不唯一）。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：

parame = {value01,value02,...}
或者
set(value)
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 这里演示的是去重功能

print('orange' in basket)                 # 快速判断元素是否在集合内
print('crabgrass' in basket)

print('-' * 30)

'''
集合的运算：
'''
a = set('abracadabra') #  集合a	
b = set('alacazam')     #  集合b	

print(a)
print(b)

print("*" * 30)
print(a-b)  # a-b（a集合中b没有的元素）

print(a|b)  # a|b(并集）

print(a&b)  # a&b(交集)

print(a^b)  # a^b(不同时包含于a和b的元素)

print('+' * 30)
'''
类似列表推导式，同样集合支持集合推导式(Set comprehension):
'''

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)