# -*- coding:UTF-8 -*-
#coding=utf-8
print "���"

for letter in "Python": #��һ��ʵ��
    print "��ǰ��ĸ��", letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits: #�ڶ���ʵ��
    print  '��ǰ��ĸ��', fruit

print "Good bye!"

#ͨ����������
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '��ǰˮ�� ��', fruits[index]

print "Good bye!"


# for -- else
for num in range(10,20):    # ���� 10 �� 20 ֮�������
    for i in range(2,num):  # �������ӵ���
        if num%i == 0:      # ȷ����һ������
            j=num/i         # ����ڶ�������
            print '%d ���� %d * %d' % (num,i,j)
            break           # ������ǰѭ��
    else:                       # ѭ����else ����
        print num, '��һ������'

#��ӡ1-9������������
for i in range(1,11):
    for k in range(1,i):
        print k,
    print '\n'

list = range(1,11)
print list


#��ӡ���ĵȱ�������
rows = int(raw_input('����������\n'))
for i in range(0, rows):
    for k in range(0, 2 * rows -1):
        if (i != rows -1) and (k == rows - i -1 or k == rows + i -1):
            print " * ",
        elif i == rows -1:
            if k % 2 == 0:
                print " * ",
            else:
                print "   ",
        else:
            print "   ",
    print "\n"
33