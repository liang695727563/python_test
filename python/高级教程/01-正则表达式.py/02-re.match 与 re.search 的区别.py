#coding=utf-8
# re.match ֻƥ���ַ����Ŀ�ʼ������ַ�����ʼ������������ʽ����ƥ��ʧ�ܣ��������� None��
# �� re.search ƥ�������ַ�����ֱ���ҵ�һ��ƥ�䡣

import re

line = "Cats are smarter than dogs";

print "re.M, re.I:" ,re.M, re.I
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
    print "search --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"
