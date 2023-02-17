#coding=utf-8
print "你好"

key1= "Alice"
value1 = '2341'
key2 = 'Beth'
value2 = '9102'
d = {key1 : value1, key2 : value2}
print d;

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}
print dict,dict2,dict2

# 访问字典里的值
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print "dict['Name']: ",dict['Name'];
print "dict['age']:", dict['Age'];
print "dict['Class']:", dict['Class'];

#修改字典
dict['Age'] = 8;    # update existing entry
dict['School'] = "DPS School"; # Add new entry

print "dict['Age']:", dict['Age'];
print "dict['Sclool'];", dict['School'];
print 'dict:', dict;

#删除字典元素
del dict['Name'];   # 删除键是'name'的条目
print 'dict:', dict;
dict.clear();       # 清空词典所有条目
print 'dict:', dict;
del dict;           # 删除词典
print 'dict', dict;
# print "dict['School']:", dict['School']

#字典键的特性
# 字典值可以没有限制地取任何 Python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1) 不允许同一个键出现两次。创建时如果同一个键被赋值两次，只会保存后一次赋值
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict['Name']:", dict["Name"];
# 2) 键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行
dict = {('Name'): 'Zara', 'Age': 7}
print "dict1['Name']:", dict['Name']
# dict = {['Name']: 'Zara', 'Age': 7} # 列表不可以作为键
# print "dict['Name']:", dict['Name']


# 实例：

# 使用Python编写字典程序：
#   用户添加单词和定义
#   查找这些单词
#   如果查不到，请让用户知道
#   循环

# 字典创建 while开关 字典添加  字典查找
dictionary = {}
flag = 'a'
page = 'a'
while flag == 'a' or 'c':
    flag = raw_input("添加或查找单词 ?(a/c)")
    if flag == 'a':                             # 开启
        word = raw_input('输入单词(key):')
        defintion = raw_input("输入定义值(value):")
        dictionary[str(word)] = str(defintion)  # 添加字典
        print "添加成功！"
        page = raw_input("你是否要查找字典?(a/0)") # read
        if page == 'a':
            print dictionary
        else:
            continue
    elif flag == 'c':
        off = 'a'
        check_word = raw_input("要查找的单词！")    # 检查
        for key in sorted(dictionary.keys()):
            if str(check_word) == key:
                print "该单词存在!", key, dictionary[key]
                break
            else:
                off = 'b'
        if off == 'b':
            print "抱歉，该值不存在！"
    else:                               # 停止
        print "error type"
        break


print "Good bye"