#coding=utf-8
class Employee:
    '����Ա���Ļ���' #���ĵ��ַ���
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
    
    def displayEmployee(self):
        print "Name ��", self.name, ",Salary: ", self.salary

# ��İ�����Ϣ����ͨ�� ClassName.__doc__�鿴��
print Employee.__doc__

# empCount ������һ�������������ֵ��������������ʵ��֮�乲����������ڲ�����ⲿ��ʹ�� Employee.empCount ���ʡ�
# ��һ�ַ��� __init__() ������һ������ķ���������Ϊ��Ĺ��캯�����ʼ����������������������ʵ��ʱ�ͻ���ø÷���
# self �������ʵ����self �ڶ�����ķ���ʱ�Ǳ����еģ���Ȼ�ڵ���ʱ���ش�����Ӧ�Ĳ�����

print '#' * 30

# self �������ʵ����������
# ��ķ�������ͨ�ĺ���ֻ��һ���ر�����𡪡����Ǳ�����һ������ĵ�һ����������, ���չ������������� self��

class Test:
    def prt(self):
        print self
        print self.__class__
    
t = Test()
t.prt()
# ��ִ�н�����Ժ����ԵĿ�����self����������ʵ��������ǰ����ĵ�ַ���� self.class ��ָ���ࡣ

# self ���� Python �ؼ��֣����ǰ������� w3cschool Ҳ�ǿ�������ִ�е�:
print "*" * 30

class Test:
    def prt(w3cschool):
        print w3cschool
        print w3cschool.__class__

t = Test()
t.prt()

print "!" *30
# Ҫ����һ�����ʵ���������ʹ��������ƣ���ͨ��__init__�������ܲ���
# ���� Employee ��ĵ�һ������
emp1 = Employee("Zara", 2000)
# ���� Employee ��ĵڶ�������
emp2 = Employee("Manni", 5000)

#������ʹ�õ� (.) �����ʶ�������ԡ�ʹ������������Ʒ��������:
emp1.displayEmployee()
emp2.displayEmployee()
print 'Total Employee %d' % Employee.empCount


print "@" * 30
# ��ӣ�ɾ�����޸��������
emp1.age = 7    # ���һ�� 'age' ����
emp1.displayEmployee()
print emp1.age
emp1.age = 8    # �޸� 'age' ����
print emp1.age
del emp1.age    # ɾ�� 'age' ����
# print emp1.age # AttributeError: Employee instance has no attribute 'age'

print '&'*30
# ��Ҳ����ʹ�����º����ķ�ʽ���������ԣ�
print hasattr(emp1, 'age')    # ������� 'age' ���Է��� True.
print setattr(emp1, 'age', 7) # ������� 'age' ֵΪ 8
print getattr(emp1, 'age')    # ���� 'age' ���Ե�ֵ
print setattr(emp1, 'age', 8) # ������� 'age' ֵΪ 8
print delattr(emp1, 'age')    # ɾ������ 'age'