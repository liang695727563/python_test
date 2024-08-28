'''
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
'''
dict = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8;               # 更新 Age
dict['School'] = "W3Cschool教程"  # 添加信息


print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

print('-' * 30)

'''
删除字典元素
​del ​能删单一的元素也能清空字典。我们可以用它来删除字典中的一组键值对也可以用来删除整个字典。
另外使用clear()也能删除字典。
'''
dict = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键 'Name'
dict.clear()     # 删除字典
del dict         # 删除字典

print ("dict['Age']: ", dict['Age'])  # 但这会引发一个异常，因为用执行 del 操作后字典不再存在：
print ("dict['School']: ", dict['School'])
