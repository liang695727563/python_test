'''
Python list 常用操作

'''
# 1.list 定义
li = ['a', 'b', 'mpilgrim', 'z', 'example']
print(li)
print(li[0])
print('-' * 30)
# 2.负数索引
print(li)
print(li[-1])
print(li[-3])
print(li)
print(li[1:3])
print(li[1:-1])
print(li[0:3])

print('+' * 30)
# 3.list 增加元素
print(li)
li.append('new')
print(li)
li.insert(2, 'new')
print(li)
li.extend(['two', 'elements'])
print(li)

print('=' * 30)
# 4.list 搜索
print(li)
print(li.index('example'))
print(li.index('new'))
# print(li.index('c'))    # valueError: 'c' is not in list
print('c' in li)

print('*' * 30)
# 5.list 删除元素
print(li)
li.remove('z')
print(li)
li.remove('new')  # 删除首次出现的一个值
print(li)
# li.remove('c')  # list 中没有找到值， Python 会引发一个异常
print(li.pop())    # pop 会做两件事：删除 list 的最后一个元素，然后返回删除元素的值。
print(li)

print('\\' * 30)
# 6.list 运算符
li = ['a', 'b', 'mpilgrim']
print(li)
li = li + ['example', 'new']
print(li)
li += ['two']
print(li)
li = [1, 2] * 3
print(li)

print('!'* 30)
# 7.使用join链接list成为字符串
params = {'server': 'mpilgrim', 'database': 'master', 'uid': 'sa', 'pwd': 'secret'}
par = ["%s=%s" % (k, v) for k, v in params.items()]
print(par)
print(";".join(par))  

'''
join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。
'''

print('-' * 30)
# 8.list 分割字符串
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ';'.join(li)
print(s)
print(s.split(';'))
print(s.split(';', 1))

'''
split 与 join 正好相反，它将一个字符串分割成多元素 list。
注意，分隔符（""）被完全去掉了，它没有在返回的 list 中的任意元素中出招。
split 接受一个可选的第二个参数，它是要分割的次数。
'''

print('+' * 30)
# 9.list 的映射解析
li = [1, 9, 8, 4]
s = [elem * 2 for elem in li]
print(li)
li = [elem * 2 for elem in li]
print(li)

print('*' * 30)
# 10.dictionary中的解析
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())

keys = [k for k, v in params.items()]
print(keys)
values = [v for k, v in params.items()]
print(values)
pra = ['%s=%s' % (k, v) for k, v in params.items()]
print(pra)

print('=' * 30)
# 11.list guolv
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
list1 = [elem for elem in li if len(elem) >1]
print(list1)
list2 = [elem for elem in li if elem != 'b']
print(list2)
list3 = [elem for elem in li if li.count(elem) ==1]
print(list3)