# -*- coding: UTF-8 -*-

# ����߳� n����ӡ��Ӧ�߳�������

# ������

# ��ӡ����
# ÿһ�д�ӡ�����ո񣬼�������
# ǰ���д�ӡ֮ǰ���뵽ջ������ջ�ĺ���ȳ�ԭ���ӡ���е�����

def diamond(n):
    stack = []
    for i in range(1, 2 * n ):
        if i <= n:
            p_str = ' ' * (n-i) + '*' * (2 * i -1)
            if i != n:
                stack.append(p_str)
            print(p_str)
        else:
            print(stack.pop())

diamond(5)