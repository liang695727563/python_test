# -*- coding:UTF-8 -*-
#coding:utf-8
print "���" 

# Ƕ�����2~100 ֮�������
i = 2
while (i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j):
        # print "{} ������",format(i)
        print "{} ������".format(i)

    i = i + 1

print "Good bye!"

#ʹ��ѭ��Ƕ������ȡ 100 ���ڵ�����
num = [];
i = 2;
for i in range(2,100):
    j = 2
    for j in range(2, i):
        if (i%j == 0):
            break
    else:
        num.append(i)
print num

# ʹ��Ƕ��ѭ��ʵ��*������ʵ��

i = 1
#j = 1
while i <= 9:
    if i <=5:
        print "*"*i
    elif i <= 9:
        j = i-2*(i-5)
        print "*"*j
    i+=1
else:
    print ""