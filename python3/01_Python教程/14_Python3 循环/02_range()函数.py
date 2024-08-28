'''
如果你需要遍历数字序列，可以使用内置 range() 函数。它会生成数列，例如:
'''
for i in range(5):
    print(i)


print('=' * 30)
'''
你也可以使用 range 指定区间的值：
'''
for i in range(5,9) :
    print(i)

print('*' * 30)

'''
也可以使 range 以指定数字开始并指定不同的增量(甚至可以是负数;有时这也叫做'步长'):
'''
for i in range(0, 10, 3):
    print(i)

print('-' * 30)
'''
负数：
'''
for i in range(-10, -100, -30) :
    print(i)

print('.' * 30)
'''
您可以结合 range() 和 len() 函数以遍历一个序列的索引,如下所示:
'''
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])

print('=' * 30)
'''
还可以使用 range() 函数来创建一个列表：
'''
b = list(range(5))
print(b)