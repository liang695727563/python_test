#coding=utf-8
# ���˽������
# __private_attrs�������»��߿�ͷ������������Ϊ˽�У�����������ⲿ��ʹ�û�ֱ�ӷ��ʡ������ڲ��ķ�����ʹ��ʱ self.__private_attrs��

# ��ķ���
# ������ڲ���ʹ�� def �ؼ��ֿ���Ϊ�ඨ��һ����������һ�㺯�����岻ͬ���෽������������� self����Ϊ��һ������

# ���˽�з���
# __private_method�������»��߿�ͷ�������÷���Ϊ˽�з���������������ⲿ���á�������ڲ����� self.__private_methods

class JustCounter:
    __secretCount = 0   # ˽�б���
    publicCount = 0     # ��������

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
# print counter.__secretCount # ����ʵ�����ܷ���˽�б���
# Python������ʵ�����������˽�����ݣ��������ʹ�� object._className__attrName �������ԣ������´����滻���ϴ�������һ�д��룺
# 
# print counter.__JustCounter__secretCount #���� һ���»���
print counter._JustCounter__secretCount

# ���»��ߡ�˫�»��ߡ�ͷβ˫�»���˵����
# __foo__: ����������ⷽ����һ����ϵͳ�������� ������ __init__() ֮��ġ�
# _foo: �Ե��»��߿�ͷ�ı�ʾ���� protected ���͵ı���������������ֻ�������䱾����������з��ʣ��������� from module import *
# __foo: ˫�»��ߵı�ʾ����˽������ (private) �ı���, ֻ������������౾����з����ˡ�
