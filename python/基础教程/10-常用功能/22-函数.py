# -*- coding: UTF-8 -*-

def printme( str ):
    "答应传入的字符串到标准显示设备上"
    print str
    return

# Now you can call printme function
printme("我要调用用户自定义函数！")
printme("再次调用同一函数")

# Python 传不可变对象实例、
def ChangeInt(a):
    a = 10

b =2
ChangeInt(b)
print b     # 结果是2

# 按值传递参数和按引用传递参数（传可变对象实例）
# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print "函数内取值：", mylist
    return

# 调用changeme函数
mylist = [10, 20, 30]
print "函数前取值：", mylist
changeme(mylist)
print "函数外取值：", mylist

# 必备参数
# printme()

# 关键字参数
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

printme( str = "My String")
# 下例能将关键字参数顺序不重要展示得更清楚：
def printinfo(name, age):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age: ", age
    return

# 调用printinfo函数
printinfo(age =50, name= 'miki')

# 缺省参数
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age: ", age
    return

printinfo(age = 50, name = 'miki')
printinfo(name = 'miki1')

# 不定长参数
# 加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出："
    print arg1
    for var in vartuple:
        print var
    return

# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# 匿名函数
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "Value of total :", sum( 10, 20)
print "Value of total :", sum( 20, 20)

# return 语句
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和
    total = arg1 + arg2
    print "Inside the function :", total
    return total

# 调用sum函数
total = sum(10, 20)
print "Outside the function:", total

# 变量作用域
total = 0 # This is global variable.

# 可写函数说明
def sum(arg1, arg2):
    # 返回两个参数的和。
    total = arg1 + arg2     # total在这里是局部变量。
    print "Inside the funtion local total : ", total
    return total

# 调用sum函数
sum(10, 20)
print "Outside the function global total :", total

