#coding=utf-8
# �ڸ����������£�������������λ(digits)��ƽ���ͣ��õ��������ٴ���������λ��ƽ���ͣ�����ظ����У����ս���ض�Ϊ 1

# �������֣�19

# �� 1 �֣�(11)+(99) =1 + 81 = 82
# �� 2 �֣�(88)+(22) =64 + 4 = 68
# �� 3 �֣�(66)+ (88) =36 + 64 = 100
# �� 4 �֣�(11) + (00) + (0*0) = 1

def sum_square(n):
    sum = 0 
    for i in str(n):
        sum += int(i) ** 2
    return sum

list1 = []
n = int(input("���������֣�"))
while sum_square(n) not in list1:
    n = sum_square(n)
    list1.append(n)

if n ==1:
    print "�ǿ�����"
else:
    print "���ǿ�����"