#coding=utf-8
# compile �������ڱ���������ʽ������һ��������ʽ�� Pattern �����󣬹� match() �� search() ����������ʹ�á�

import re

print 'began'

pattern = re.compile(r'\d+')                # ����ƥ������һ������
m = pattern.match('one12twothree34four')    # ����ͷ����û��ƥ��
print m             # None

m = pattern.match('one12twothree34four', 2, 10) # ��'e'��λ�ÿ�ʼƥ�䣬û��ƥ��
print m             # None

m = pattern.match('one12twothree34four', 3, 10) # ��'1'��λ�ÿ�ʼƥ�䣬����ƥ��
print m             # ����һ�� Match ����

m.group(0)          # ��ʡ�� 0
print m.group(0)

print m.start(0)    # ��ʡ�� 0

print m.end(0)      # ��ʡ�� 0

print m.span(0)     # ��ʡ�� 0 

print '*' * 30


import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I ��ʾ���Դ�Сд
m = pattern.match('Hello world Wide Web')
print m     # ƥ��ɹ�������һ�� Match ����

print m.group(0)    # ����ƥ��ɹ��������Ӵ�
print m.span(0)     # ����ƥ��ɹ��������Ӵ�������
print m.group(1)    # ���ص�һ������ƥ��ɹ����Ӵ�
print 'm.span(1):',m.span(1)     # ���ص�һ������ƥ��ɹ����Ӵ���suoy
print m.group(2)    # ���صڶ�������ƥ��ɹ����Ӵ�
print m.span(2)     # ���صڶ�������ƥ��ɹ����Ӵ�
print m.groups()    # �ȼ��� (m.group(1), m.group(2),...)

print m.group(3)    # �����ڵ�����fenzk
