# -*- coding: UTF-8 -8-
print "���"

var1 = 'Hello World!'
var2 = "Python w3cschool"

# Python�����ַ����е�ֵ
# Python��֧�ֵ��ַ����ͣ����ַ�Ҳ��PythonҲ����Ϊһ���ַ���ʹ�á�

# Python�������ַ���������ʹ�÷���������ȡ�ַ���������ʵ����
print "var1[0]:", var1[0]
print 'var2[1:5]', var2[1:5]
print "var2[:1]", var2[:1]
print "var2[0:1]", var2[0:1]
print "var2[1:1]", var2[1:1]
print "var2[1:2]", var2[1:2]
print "var2[0:2]", var2[0:2]

# ����Զ��Ѵ��ڵ��ַ��������޸ģ�����ֵ����һ������������ʵ����
var1 = 'Hello World!'
var2 = var1[:6] + 'w3cschool!'

print 'var1:',var1
print "�����ַ���var2:-",var2

# �ַ��������
a = 'Hello'
b = 'Python'

print "a + b ��������", a + b
print "a * 2 ��������", a * 2
print 'a[1] ��������', a[1]
print 'a[1:4] ��������', a[1:4]
if ( 'H' in a):
    print "H �ڱ��� a ��"
else:
    print "H ���ڱ��� a ��"

if "M" not in a:
    print "M ���ڱ��� a ��"
else:
    print "M �ڱ��� a ��"

print r'\n'
print R"\n"

# Python ֧�ָ�ʽ���ַ�������� 

print "My name is %s and weight is %d kg" % ("Zara",21)

# Python ����������һ���ַ�������У��ַ����п��԰������з����Ʊ���Լ����������ַ���

# �����ŵ��﷨��һ�������ĵ����Ż���˫���ţ�ͨ�����ǳɶԵ��ã�
hi = '''hi
there'''

print hi

# Unicode �ַ���
un = u'Hello World !'
print un
# ����ǰСд��"u"��ʾ���ﴴ������һ�� Unicode �ַ���������������һ�������ַ�������ʹ�� Python �� Unicode-Escape ���롣��������ʾ��
un2 = u'Hello\u0020World !'
print un2
