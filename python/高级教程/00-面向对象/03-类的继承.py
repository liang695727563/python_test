#coding=utf-8
# ע�⣺ͨ������Ҫ�ڵ������ļ��ж���һ���࣬

# �� Python �м̳��е�һЩ�ص㣺

# 1���ڼ̳��л���Ĺ��죨__init__()���������ᱻ�Զ����ã�����Ҫ����������Ĺ���������ר�ŵ��á�
# 2���ڵ��û���ķ���ʱ����Ҫ���ϻ��������ǰ׺������Ҫ����self���������������������е�����ͨ����ʱ������Ҫ����self����
# 3��Python�������Ȳ��Ҷ�Ӧ���͵ķ�������������������������ҵ���Ӧ�ķ��������ſ�ʼ��������������ҡ������ڱ����в��ҵ��õķ������Ҳ�����ȥ�������ң���
# ����ڼ̳�Ԫ��������һ�����ϵ��࣬��ô���ͱ�����"���ؼ̳�" ��

class Parent:       # ���常��
    parentAttr = 100
    def __init__(self):
        print "���ø��๹�캯��"

    def parentMethod(self):
        print "���ø��෽��"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "�������� :", Parent.parentAttr


class Child(Parent):    # ��������
    def __init__(self):
        print "��������Ĺ��췽��"

    def childMethod(self):
        print "�������෽�� child method"
    

c =Child()          # ʵ��������
c.childMethod()     # ��������ķ���
c.parentMethod()    # ���ø��෽��
c.setAttr(200)      # �ٴε��ø���ķ���
c.getAttr()         # �ٴε��ø���ķ���

# �����ʹ�� issubclass() ���� isinstance() ��������⡣

# issubclass() - ���������ж�һ��������һ�����������������࣬�﷨��issubclass(sub,sup)
# isinstance(obj, class) �����������obj��Class���ʵ�����������һ�� class �����ʵ�������򷵻� true��
