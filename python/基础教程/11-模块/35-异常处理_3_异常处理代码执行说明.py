# coding=utf-8

# �쳣�������ִ��˵��
# This is note foe exception

try:
    code    # ��Ҫ�ж��Ƿ���׳��쳣�Ĵ��룬���û���쳣����python��ֱ��ִֹͣ�г���

except: # ����Ჶ׽����������е��쳣���������쳣�׳��쳣������Ϣ
# except ExceptinoName arg�� # ͬʱҲ���Խ����쳣���ƺͲ�������Բ�ͬ��ʽ���쳣����

    code    # ����ִ���쳣�������ش��룬��ӡ�����

else:   # ���û���쳣��ִ��else

    code    # try���ֱ�����ִ�к�ִ�еĴ���

finally��
    code    # �˳�try�����ִ�еĳ���

# ���������쳣���
def try_exception(num):
    try:
        return int(num)
    except ValueError, arg:
        print arg, "is not a mumber"
    else:
        print "this is a number inputs"

try_exception('xxx')

# ����쳣ֵ
Invalide literal for int() with base 10: 'xxx' is not a number