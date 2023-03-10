#coding=utf-8
class Employee:
    '所有员工的基类' #类文档字符串
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
    
    def displayEmployee(self):
        print "Name ：", self.name, ",Salary: ", self.salary

# 类的帮助信息可以通过 ClassName.__doc__查看。
print Employee.__doc__

# empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
# 第一种方法 __init__() 方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
# self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。

print '#' * 30

# self 代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

class Test:
    def prt(self):
        print self
        print self.__class__
    
t = Test()
t.prt()
# 从执行结果可以很明显的看出，self代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。

# self 不是 Python 关键字，我们把他换成 w3cschool 也是可以正常执行的:
print "*" * 30

class Test:
    def prt(w3cschool):
        print w3cschool
        print w3cschool.__class__

t = Test()
t.prt()

print "!" *30
# 要创建一个类的实例，你可以使用类的名称，并通过__init__方法接受参数
# 创建 Employee 类的第一个对象
emp1 = Employee("Zara", 2000)
# 创建 Employee 类的第二个对象
emp2 = Employee("Manni", 5000)

#您可以使用点 (.) 来访问对象的属性。使用如下类的名称访问类变量:
emp1.displayEmployee()
emp2.displayEmployee()
print 'Total Employee %d' % Employee.empCount


print "@" * 30
# 添加，删除，修改类的属性
emp1.age = 7    # 添加一个 'age' 属性
emp1.displayEmployee()
print emp1.age
emp1.age = 8    # 修改 'age' 属性
print emp1.age
del emp1.age    # 删除 'age' 属性
# print emp1.age # AttributeError: Employee instance has no attribute 'age'

print '&'*30
# 你也可以使用以下函数的方式来访问属性：
print hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True.
print setattr(emp1, 'age', 7) # 添加属性 'age' 值为 8
print getattr(emp1, 'age')    # 返回 'age' 属性的值
print setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
print delattr(emp1, 'age')    # 删除属性 'age'