#coding=utf-8
#���������

# �������һ�� 100 ���ڵ����������� 10 �λ��Ὺʼ��Ϸ������²�����֡�

# �����С�ˣ�����ʾ����С��
# ����´��ˣ�����ʾ���´���
# �¶��ˣ�����ʾ���¶��ˣ����ҽ�����Ϸ
# 10 �λ������껹û�¶ԣ���ʾ����Ϸ������û�вµ���

import random as rd;

number = rd.randint(0, 100)
for i in range(10):
    choice = int(input("��������Ҫ�²�����֣�"))
    if choice > number:
        print "��´���"
    elif choice < number:
        print "���С��"
    else:
        print "��¶��ˣ������"
        print "��һ������"  , i+1 , "�λ���"
        break
    print "��ʣ", 9-i, "�λ���"
else:
    print "��Ϸ��������û�вµ�"
