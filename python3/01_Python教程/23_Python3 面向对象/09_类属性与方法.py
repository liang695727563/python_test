'''
类属性与方法
类的私有属性
__private_attrs: 两个下划线开头，声明该属性为私有，不能再类地外部被使用或直接访问。
在类内部的方法中使用时 self.__private_attrs.

类的方法
在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数

类的私有方法
__private_method: 两个下划线开头，生命该方法为私有方法，不能再类的外部调用。再类的内部调用 self.__private_method.

'''
class JustCounter:
    __secretCount = 0   # 私有变量
    publicCount = 0     # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)    # 报错，实例不能访问私有变量

'''
类的专有方法：
__init__: 构造函数，在生成对象时调用
__del__: 析构函数，释放对象时使用
__repr__: 打印，转换
__setitem__: 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获取长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方

运算符重载
Python 同样支持运算符重载，那么可以对类的专有方法进行重载。

'''
print('-'* 30)
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector (%d, %d)" %(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


