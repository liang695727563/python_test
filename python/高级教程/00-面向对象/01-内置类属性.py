#coding=utf-8
class Employee:
    '����Ա���Ļ���'
    empCount = 0

    def __init__(self, name, salary): #���캯�����ʼ�������� selfΪ Ĭ�϶��巽������������贫����
        self.name = name
        self.selary = salary
        Employee.empCount += 1

    def displayCount(self):
        print 'Total Employee %d' % Employee.empCount

    def displayEmployee(self):
        print 'Name: ', self.name , ', Salary: ', salf.salary

print "Employee.__doc__:", Employee.__doc__     # ����ĵ��ַ���
print "Employee.__name__:", Employee.__name__   # ����
print "Employee.__module__", Employee.__module__    # �ඨ�����ڵ�ģ�飨���ȫ����'__main__.className',�����λ��һ������ģ��mymod�У���ô className__module__ ����mymod��
print "Employee.__bases__:", Employee.__bases__     # ������и��๹��Ԫ�أ��������Ը������и�����ɵ�Ԫ�飩
print "Employee.__dict__:", Employee.__dict__       # ������ԣ�����һ���ֵ䣬���������������ɣ�
