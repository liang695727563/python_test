# coding=utf-8
# ����˼�룺��δ������������ҵ�һ����С��Ԫ�أ��ŵ���һλ���ٴ�ʣ��δ������������ҵ���С��Ԫ�أ��ŵ��ڶ�λ���������ƣ�ֱ������Ԫ�ض��������

import random as rd

sec_list = [rd.randint(1,100) for i in range(8)]

length = len(sec_list)
print "δ������б�Ϊ��",sec_list

for i in range(length -1):
    min_index = i
    for j in range(i +1,length):
        if sec_list[min_index] > sec_list[j]:
            min_index = j 
    sec_list[min_index], sec_list[i] = sec_list[i], sec_list[min_index]
    print "��",i+1,"���ź�����:",sec_list
print "�����ź�����б�Ϊ��",sec_list