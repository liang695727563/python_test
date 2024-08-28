'''
在Python3中字典（dictionary ，简写为dict）是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 (​key=>value​) 对用冒号 (:) 分割，每个对之间用逗号 (,) 分割，整个字典包括在花括号 (​{}​) 中 ,
格式如下所示：
dict = {key1 : value1, key2 : value2 }
示例：
 key（键）	value（值） 
 'Alice'	'2341' 
 'Beth'	'9102' 
 'Cecil'	'3258' 
 'Danna'	'2341' 
 'Steven'	'5643' 

 键必须是唯一的，但值则不必(上表中Danna和Alice的键是不同的，值却是相同的)。

值可以取任何数据类型，但​键必须是不可变的​，如字符串，数字或元组。
'''

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'} # 一个简单的字典实例

# 也可如此创建字典：
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }

'''
访问字典里的值
与列表取值类似，但列表取值时使用索引，字典取值时使用key
'''
dict = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

print('*' * 30)

dict = {'Name': 'W3CSchool', 'Age': 7, 'Class': 'First'}
 
print ("dict['Alice']: ", dict['Alice'])  # 如果用字典里没有的键访问数据，会输出错误
