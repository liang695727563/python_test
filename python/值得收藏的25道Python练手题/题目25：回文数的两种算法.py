#coding=utf-8
# ��������ָ����(��������)�͵���(��������)����һ�������������磬1221 �ǻ��ģ��� 1222 ���ǡ�

# �ⷨһ��ͨ����ת�ַ������бȶ�
def is_palindrome(x):
    if x < 0 or x > 0 and x % 10 == 0:
        return False
    str_x = str(x)
    return str_x == str_x[::-1]

print is_palindrome(121)
print is_palindrome(120)

print '*' *30
# �ⷨ������תһ�����ֺ�ǰ�벿�ֵ����ֽ��бȽ�
# ����

# �������� x������벿�ַ�ת�����浽���� reverted
# ÿ��ѭ�� x%10 �õ�ĩβ����
# Ȼ�� x/10 ȥ��ĩβ������
# ѭ���������� x<=reverted
# ���ֳ��ȣ������� 12321
# ���ֳ��ȣ�ż���� 1221

def is_palindrome2(x):
    if x < 0 or x > 0 and x % 10 == 0:
        return False
    reverted = 0
    while x > reverted:
        # ���ǿ��� 1221
        # ��һ��ѭ��������Ҫ��ĩβ����1ȡ���� �ڶ���ȡĩβ����2 ������Ҫ��21���12
        reverted = reverted * 10 + x % 10
        # ��x��ĩβ����ɾ����
        x //= 10
    return x == reverted or x == reverted // 10

print is_palindrome2(1221)
print is_palindrome2(1223)
print is_palindrome2(123321)