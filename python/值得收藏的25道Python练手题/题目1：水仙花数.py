
#coding=utf-8
# ˮ�ɻ�����Narcissistic number��Ҳ����Ϊ����ȫ���ֲ�������pluperfect digital invariant, PPDI����������������������ķ˹׳����ķ˹��������Armstrong number��

# ˮ�ɻ�����ָһ�� 3 λ��������ÿ��λ�ϵ����ֵ� 3 ����֮�͵������������磺1^3 + 5^3+ 3^3 = 153��


for i in range(100,1000):
    i1 = i // 100       # ȡ��λ���� 123//100=1
    i2 = i // 10 % 10   # ȡʮλ���� 123//10=12 12%10 =2
    i3 = i % 10         # ȡ��λ���� 123%10=3

    if i1 ** 3 + i2 ** 3 + i3 ** 3 == i:
        print  i,"��ˮ�ɻ���"


# https://mp.weixin.qq.com/s/9RdeRVggEsutTLzcuHS5Qg