# Python 3 支持 int（整型）、float（浮点型）、bool（布尔型）、complex（复数）。

# 置的 type() 函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# 此外还可以用isinstance来判断：
print(isinstance(a, int))
print(isinstance(b, int))

print('-------------------------------------------')
'''
isinstance和type的区别在于：

type（）不会认为子类是一种父类类型。
isinstance（）会认为子类是一种父类类型。
'''
class A:
     name =''

class B(A):
    age = 0

print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

print("************************")

'''
注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

当你指定一个值时，Number 对象就会被创建：
'''
var1 = 1
var2 = 10
var3 = 11

# 使用 del 语句删除一些对象引用。
del var1
del var2, var3

print("+" * 18)

# 数值运算：
print(5 + 4) # 加法
print(4.3 - 2)  # 减法
print(3 * 7) # 乘法
print(2 / 4 ) # 除法，得到一个浮点数
print(2 // 4) # 出发，得到一个整数
print(17 % 3) # 取余
print(2 ** 5) # 乘方

'''
注意：

1、Python 可以同时为多个变量赋值，如 a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法（/）总是返回一个浮点数，要获取整数使用​//​操作符。
4、在混合计算时，Python 会把整型转换成为浮点数。
'''