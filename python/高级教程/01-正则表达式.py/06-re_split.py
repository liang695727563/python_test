#coding=utf-8
# split ���������ܹ�ƥ����Ӵ����ַ����ָ�󷵻��б�

import re

print re.split('\W+', 'w3cschool, w3cschool,w3cschool.')
print re.split('(\W+)',' w3cschool,w3cschool,w3cschool.')
print re.split('\W+',' w3cschool, w3cschool,w3cschool.', 1)

print re.split('a*', 'hello world')     # ����һ���Ҳ���ƥ����ַ������ԣ�split ������������ָ�
