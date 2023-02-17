# -*- coding: UTF-8 -8-
print "你好"

var1 = 'Hello World!'
var2 = "Python w3cschool"

# Python访问字符串中的值
# Python不支持单字符类型，单字符也在Python也是作为一个字符串使用。

# Python访问子字符串，可以使用方括号来截取字符串，如下实例：
print "var1[0]:", var1[0]
print 'var2[1:5]', var2[1:5]
print "var2[:1]", var2[:1]
print "var2[0:1]", var2[0:1]
print "var2[1:1]", var2[1:1]
print "var2[1:2]", var2[1:2]
print "var2[0:2]", var2[0:2]

# 你可以对已存在的字符串进行修改，并赋值给另一个变量，如下实例：
var1 = 'Hello World!'
var2 = var1[:6] + 'w3cschool!'

print 'var1:',var1
print "更新字符串var2:-",var2

# 字符串运算符
a = 'Hello'
b = 'Python'

print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
print 'a[1] 输出结果：', a[1]
print 'a[1:4] 输出结果：', a[1:4]
if ( 'H' in a):
    print "H 在变量 a 中"
else:
    print "H 不在变量 a 中"

if "M" not in a:
    print "M 不在变量 a 中"
else:
    print "M 在变量 a 中"

print r'\n'
print R"\n"

# Python 支持格式化字符串的输出 

print "My name is %s and weight is %d kg" % ("Zara",21)

# Python 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。

# 三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）
hi = '''hi
there'''

print hi

# Unicode 字符串
un = u'Hello World !'
print un
# 引号前小写的"u"表示这里创建的是一个 Unicode 字符串。如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：
un2 = u'Hello\u0020World !'
print un2
