#coding=utf-8
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary): #构造函数或初始化函数， self为 默认定义方法必填，调用无需传参项
        self.name = name
        self.selary = salary
        Employee.empCount += 1

    def displayCount(self):
        print 'Total Employee %d' % Employee.empCount

    def displayEmployee(self):
        print 'Name: ', self.name , ', Salary: ', salf.salary

print "Employee.__doc__:", Employee.__doc__     # 类的文档字符串
print "Employee.__name__:", Employee.__name__   # 类名
print "Employee.__module__", Employee.__module__    # 类定义所在的模块（类的全名是'__main__.className',如果类位于一个导入模块mymod中，那么 className__module__ 等于mymod）
print "Employee.__bases__:", Employee.__bases__     # 类的所有父类构成元素（包含了以个由所有父类组成的元组）
print "Employee.__dict__:", Employee.__dict__       # 类的属性（包含一个字典，由类的数据属性组成）
