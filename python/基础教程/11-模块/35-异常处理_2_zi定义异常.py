# coding=utf-8

# ͨ������һ���µ��쳣�࣬����������������Լ����쳣��
# �쳣Ӧ���ǵ��͵ļ̳��� Exception �࣬ͨ��ֱ�ӻ��ӵķ�ʽ��
# �û��Զ����쳣 ����Ϊ RuntimeError
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

# �������Զ����쳣
try:
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.args
print "�Զ����쳣չʾ���"


