# -*- coding: UTF-8 -*-

def printme( str ):
    "��Ӧ������ַ�������׼��ʾ�豸��"
    print str
    return

# Now you can call printme function
printme("��Ҫ�����û��Զ��庯����")
printme("�ٴε���ͬһ����")

# Python �����ɱ����ʵ����
def ChangeInt(a):
    a = 10

b =2
ChangeInt(b)
print b     # �����2

# ��ֵ���ݲ����Ͱ����ô��ݲ��������ɱ����ʵ����
# ��д����˵��
def changeme(mylist):
    "�޸Ĵ�����б�"
    mylist.append([1,2,3,4])
    print "������ȡֵ��", mylist
    return

# ����changeme����
mylist = [10, 20, 30]
print "����ǰȡֵ��", mylist
changeme(mylist)
print "������ȡֵ��", mylist

# �ر�����
# printme()

# �ؼ��ֲ���
# ʹ�ùؼ��ֲ�������������ʱ������˳��������ʱ��һ�£���Ϊ Python �������ܹ��ò�����ƥ�����ֵ��

printme( str = "My String")
# �����ܽ��ؼ��ֲ���˳����Ҫչʾ�ø������
def printinfo(name, age):
    "��ӡ�κδ�����ַ���"
    print "Name: ", name
    print "Age: ", age
    return

# ����printinfo����
printinfo(age =50, name= 'miki')

# ȱʡ����
def printinfo(name, age=35):
    "��ӡ�κδ�����ַ���"
    print "Name: ", name
    print "Age: ", age
    return

printinfo(age = 50, name = 'miki')
printinfo(name = 'miki1')

# ����������
# �����Ǻţ�*���ı�������������δ�����ı���������ѡ�񲻶ഫ����Ҳ��
def printinfo(arg1, *vartuple):
    "��ӡ�κδ���Ĳ���"
    print "�����"
    print arg1
    for var in vartuple:
        print var
    return

# ����printinfo ����
printinfo(10)
printinfo(70, 60, 50)

# ��������
# ��д����˵��
sum = lambda arg1, arg2: arg1 + arg2;

# ����sum����
print "Value of total :", sum( 10, 20)
print "Value of total :", sum( 20, 20)

# return ���
# ��д����˵��
def sum(arg1, arg2):
    # ����2�������ĺ�
    total = arg1 + arg2
    print "Inside the function :", total
    return total

# ����sum����
total = sum(10, 20)
print "Outside the function:", total

# ����������
total = 0 # This is global variable.

# ��д����˵��
def sum(arg1, arg2):
    # �������������ĺ͡�
    total = arg1 + arg2     # total�������Ǿֲ�������
    print "Inside the funtion local total : ", total
    return total

# ����sum����
sum(10, 20)
print "Outside the function global total :", total

