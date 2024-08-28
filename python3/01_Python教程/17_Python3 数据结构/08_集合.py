'''
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。

可以用大括号 ({}) 创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)       # show that duplicates have been removed
print('orange' in basket)  # fast membership testing
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)        # unique letters in a
print(a - b)    # letters in a but not in b
print(a | b)    # letters in either a or b
print(a & b)    # letters in both a and b
print(a ^ b)    # letters in a or b but not both

print('*' * 30)
# 集合也支持推导式：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)