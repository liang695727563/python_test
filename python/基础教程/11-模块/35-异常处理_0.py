#coding=utf-8

# ���쳣���
try:
    fh = open("testfile","w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "Error: can\'t find file or read data"
else:
    print "Written content in the file successfully"
    fh.close()

print "Good bey"

# �������ļ��޸�Ϊֻ�����ᱨ�쳣

# ʹ��except �������κ��쳣���ͣ� 
# try-except��䲶�����з������쳣�����ⲻ��һ���ܺõķ�ʽ�����ǲ���ͨ���ó���ʶ���������쳣��Ϣ����Ϊ���������е��쳣

# try-finally ��������Ƿ����쳣����ִ�����Ĵ��롣

'''
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print "finally-Error: can\'t find file or read data"

print "finally end"
# finally ���е��������ִ�к��쳣���ٴ��������ִ��except �����
'''

