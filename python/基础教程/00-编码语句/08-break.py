# -*- coding: UTF-8 -*-
#coding=utf-8
print "���"

for letter in 'Python':     # ��һ��ʵ��
    if letter == 'h':
        break
    print '������ĸ��', letter


var = 10                    # �ڶ���ʵ��
while var > 0:
    print '���ڱ���ֵ��', var
    var = var -1
    if var == 5:    # ������ var ���� 5 ʱ�˳�ѭ��
        break
print "Good bye!"