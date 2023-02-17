# --*-- coding: utf-8 --*--

# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：

class Parent:           # 定义父类
    def myMethod(self):
        print "调用父类方法"

class Child(Parent):    # 定义子类
    def myMethod(self):
        print "调用子类方法"

c = Child()     # 子类实例
c.myMethod()    # 子类调用重写方法

# ++++++++++++++++++++++++++++++++++++++++++++++

# 下表列出了一些通用的功能，你可以在自己的类重写：

# 序号	方法, 描述 & 简单的调用
# 1	__init__ ( self [,args...] )
# 构造函数
# 简单的调用方法: obj = className(args)
# 2	__del__( self )
# 析构方法, 删除一个对象
# 简单的调用方法 : dell obj
# 3	__repr__( self )
# 转化为供解释器读取的形式
# 简单的调用方法 : repr(obj)
# 4	__str__( self )
# 用于将值转化为适于人阅读的形式
# 简单的调用方法 : str(obj)
# 5	__cmp__ ( self, x )
# 对象比较
# 简单的调用方法 : cmp(obj, x)