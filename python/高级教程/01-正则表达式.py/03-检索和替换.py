#coding=utf-8
# Python �� re ģ���ṩ�� re.sub �����滻�ַ����е�ƥ���

import re

phone = "2004-959-559 # ����һ������绰����"

# ɾ���ַ��е� Pythonע��
num = re.sub( r'#.*$', "", phone)
print "�绰�����ǣ�", num

# ɾ�������֣�-�����ַ���
num = re.sub( r'\D', "", phone)
print "�绰�����ǣ�", num

# re.sub(pattern, repl, string, max=0)
# ���ص��ַ��������ַ������� RE ����߲��ظ���ƥ�����滻�����ģʽû�з��֣��ַ�����û�иı�ط��ء�

# ��ѡ���� count ��ģʽƥ����滻����������count �����ǷǸ�������ȱʡֵ�� 0 ��ʾ�滻���е�ƥ�䡣
# repl ������һ������

# ��ƥ������ֳ��� 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print re.sub('(?P<value>\d+)', double, s)