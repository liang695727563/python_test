#coding=utf-8
# ���ַ������ҵ�������ʽ��ƥ��������Ӵ���������һ���б����û���ҵ�ƥ��ģ��򷵻ؿ��б�
# ע�⣺ motch �� search ��ƥ��һ�� findall ƥ������

import re;

pattern = re.compile(r'\d+')    # ��������
result1 = pattern.findall('school 123 google 456')
result2 = pattern.findall('sch88ool123gogle456', 0, 10)

print result1
print result2

print '*'*30

# re.finditer
# ��findall���ƣ����ַ������ҵ�������ʽ��ƥ��������Ӵ�������������Ϊһ�����������ء�

import re

it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print match.group()