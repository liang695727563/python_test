'''
类对象
类对象支持两种操作：属性引用和实例化。
属性引用使用和 Python 中所有的属性引用一样的标准语句：obj.name。
类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样；
'''
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'Hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

# 以上创建了一个新的类实例并将该对象赋给局部变量 x，下为空的对象。

'''
很多类都倾向于将对象创建为由初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）。
像这样：
def __init__():
    self.data = []

类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法。
所以在下列中，可以这样创建一个新的实例：

x = MyClass()

当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。
'''
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r,x.i)


