#coding=utf-8
# һ���������Ľ׳�(factorial)������С�ڼ����ڸ�����������֮�������� 0 �Ľ׳�Ϊ 1

# �� 5!=12345 ���� 1!+2!+3!+4!+5!+��+10! ��ѧ���ʽ��f(n) = n*f(n-1)��

def factor(n):
    if n < 2:
        return 1
    return n * factor(n -1)

s_sum = 0 
for i in range(1, 11):
    s_sum += factor(i)
print s_sum