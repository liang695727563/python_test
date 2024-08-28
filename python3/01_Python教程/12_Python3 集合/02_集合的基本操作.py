'''
1、添加元素  语法格式： s.add( x )
将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
'''
thisset = set(("Google", "W3Cschool", "Taobao"))
thisset.add("Baidu")
print(thisset)

'''
还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
s.update( x )
x 可以有多个，用逗号分开。
'''
thisset = set(("Google", "w3Cschool", "Taobao"))
thisset.update({1,3})
print(thisset)
thisset.update([1,4],[5,6])  
print(thisset)

print('-' * 30)

'''
2、移除元素  语法格式  s.remove( x )
将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
'''

thisset = set(("Google", "W3Cschool", "Taobao"))
thisset.remove("Taobao")
print(thisset)

# thisset.remove("Facebook")   # 不存在会发生错误

'''
此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
s.discard( x )
'''

thisset = set(("Google", "W3Cschool", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)

'''
我们也可以设置随机删除集合中的一个元素，语法格式如下：
s.pop() 
'''
thisset = set(("Google", "W3Cschool", "Taobao", "Facebook"))
x = thisset.pop()

print(x)
print(thisset)

'''
多次执行测试结果都不一样。

set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。
因为这个过程是不确定的，所以删除结果也是不确定的，不建议使用这种方式进行删除。
'''
print('+' * 30)
'''
3、计算集合元素个数  语法格式：len(s)
计算集合 s 的元素个数。
'''
thisset = set(("Google", "W3Cschool", "Taobao"))
print(len(thisset))

print('*' * 30)

'''
4、清空集合     语法格式：s.clear()
清空集合 s。
'''
thisset = set(("Google", "W3cschool", "Taobao"))
thisset.clear()
print(thisset)

print('=' * 30)

'''
5、判断元素是否在集合中存在     语法格式：x in s
判断元素 x 是否在集合 s 中，存在则返回 True，不存在则返回 False。
'''

thisset = set(("Google", "W3Cschool", "Taobao"))
print("W3Cschool" in thisset)
print("Facebook" in thisset)