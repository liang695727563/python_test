# -*- coding:UTF-8 -*-
#coding=utf-8
print '���'

count = 0
while count < 9:
    print 'The count is:', count
    count =count +1
print 'Good bye!'

''''''''''''
#coding=utf-8
#continue �� break �÷�

i=1
while i < 10:
    i +=1
    if i%2  >0:     # ��˫��ʱ�������
        continue
    print i         # ���˫��2��4��6��8��10

i = 1
while 1:        # ѭ������Ϊ1�ض�����
    print i     # ���1-10
    i += 1
    if i > 10:  # ��i����10ʱ����ѭ��
        break


""""""""""""
"""

var = 1
while var == 1:  # ��������ԶΪtrue��ѭ��������ִ����ȥ
    num = raw_input("Enter a number :")
    print "You entered: ",num

print "Cood bye!"

"""

''''''''''''''

count  = 0
while count < 5:
    print count , ' is less than 5'
    count = count +1
else:
    print count ,' is not less than 5'

''''''''
# while���д���
flag = 1

# while (flag): print 'Given flag is really true!'

print "Good bye!"


''''''''''''

# coding=utf-8
#һ���򵥵�ʹ��whileȥ���ַ���ǰ��ո�Ĵ���
str = '      W3cschool    '
#��ӡ���д���ǰ���ַ���
print str

#ʹ��ѭ��ȥ���ַ���ǰ�Ŀո�
while str[:1] == ' ':
    str = str[1:]
#ʹ��ѭ����ȥ�ַ�����Ŀո�
while str[-1] == ' ':
    str = str[:-1]
# ��ӡ�����Ľ��
print str