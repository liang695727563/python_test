# -*- coding: UTF-8 -*-
#coding=utf-8
for letter in 'Python':     # ��һ��ʵ��
    if letter == 'h':
        continue
    print '��ǰ��ĸ��', letter


var = 10                    # �ڶ���ʵ��
while var > 0:
    var = var -1
    if var == 5:
        continue
    print '��ǰ������', var
print "Cood bye!"


n = 0
while n < 10:
    n = n +1
    if n % 2 == 0 :         # ���n��ż����ִ��continue���
        continue            # continue ����ֱ�Ӽ�����һ��ѭ����������print() ��䲻��ִ��
    print(n)
