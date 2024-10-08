'''
方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法。
'''

class Parent:       # 定义父类
    def myMethod(self):
        print("调用父类方法")

class Child(Parent): # 定义子类
    def myMethod(self):
        print('调用子类方法')

c = Child()     # 子类实例
c.myMethod()    # 子类调用重写方法