# -*- coding:utf-8 -*-

# �쳣�Ĳ���
# һ���쳣���Դ��ϲ���������Ϊ������쳣��Ϣ����

# ���庯��
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "The argument does not contain numbers\n", Argument

# ���ú���
temp_convert("xyz")
print "Argument end"

# �����쳣
# ���ǿ���ʹ��raise ����Լ������쳣

# ����һ���쳣
def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # �����쳣�󣬺���Ĵ���Ͳ�����ִ��

# ע�⣺Ϊ���ܹ������쳣��"except"������������ͬ���쳣���׳����������ַ�����
# ����Ҫ���������쳣����except��������£�
try:
    print "Business Logic here..."
    functionName("-2")
    # functionName(0)
except "Invalid level!":
    print "Exception handling here..."
else:
    print "Rest of the code here..."