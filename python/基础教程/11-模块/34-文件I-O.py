# -*- coding: UTF-8 -*-
# Python �ļ� I/O

# ��ӡ����Ļ
print "Python is really a great language,", "isn't it?";

# ��ȡ��������
# Python �ṩ���������ú����ӱ�׼�������һ���ı���Ĭ�ϵı�׼�����Ǽ���

# raw_input() �����ӱ�׼�����ȡһ���У�������һ���ַ�����ȥ����β�Ļ��з���
str = raw_input("�����룺");
print "������������ǣ�", str

print "������������������������������������������������"
# input() ������ raw_input() �����������Ի�����
# ���� input�������������һ����Ч��Python���ʽ��������������
str = input("Enter your input��");
print "Received input is : ", str

print "++++++++++++++++++++++++"

# �򿪺͹ر��ļ�
# open����
# �������� Python ���õ� open() ������һ���ļ�������һ�� file ������صĸ��������ſ��Ե��������ж�д��
# �﷨�� file object = open(file_name [, access_mode][, buffering])

# ��һ���ļ�
fo = open("foo.txt", "wb")
print "�ļ�����", fo.name
print "�Ƿ��ѹرգ�", fo.closed
print "����ģʽ��", fo.mode
# print "ĩβ�Ƿ�ǿ�Ƽӿո�", fo.softspace

# �رմ򿪵��ļ�
fo.close()

print "open�ļ���"
# ��һ���ļ�
# fo = open("E:/python/11-ģ��/tmp/foo.txt", "wb")
# fo = open("/tmp/foo.txt","wb") # ���λ��Ϊʲô�Ҳ����ļ�
# fo = open("E:/foo.txt", "wb")
fo = open("foo.txt", "wb")
fo.write("Python is a great language.\nYeah ite great!!\n");

# �رմ򿪵��ļ�
fo.close()

print "read file:"
# read() ����

# ��һ���ļ�
fo = open("foo.txt", "r+")
str = fo.read(10);
print "��ȡ���ַ����ǣ�", str
# �رմ򿪵��ļ�
fo.close()