#coding=utf-8
# ������ʽ��һ��������ַ����У����ܰ����㷽��ļ��һ���ַ����Ƿ���ĳ��ģʽƥ�䡣Python �� 1.5 �汾�������� re ģ�飬���ṩ Perl ����������ʽģʽ��

# re ģ��ʹ Python ����ӵ��ȫ����������ʽ���ܡ�

# compile ��������һ��ģʽ�ַ����Ϳ�ѡ�ı�־��������һ��������ʽ���󡣸ö���ӵ��һϵ�з�������������ʽƥ����滻��

# re ģ��Ҳ�ṩ������Щ����������ȫһ�µĺ�������Щ����ʹ��һ��ģʽ�ַ�����Ϊ���ǵĵ�һ��������

import re

line = "Cate are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# ƥ��ɹ� re.match ��������һ��ƥ��Ķ��󣬷��򷵻� None��

# ���ǿ���ʹ�� group(num) �� groups() ƥ�����������ȡƥ����ʽ��
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"

print '*' *30

# re.search �����ַ����ڲ���ģʽƥ�䣬ֱ���ҵ���һ��ƥ�䡣
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print "searchObj.group() : ", searchObj.group()
    print "searchObj.group(1) : ", searchObj.group(1)
    print "searchObj.group(2) : ", searchObj.group(2)
else:
    print "Nothing found!!"

# re.match �� re.search ������
# re.match ֻƥ���ַ����Ŀ�ʼ������ַ�����ʼ������������ʽ����ƥ��ʧ�ܣ��������� None���� re.search ƥ�������ַ�����ֱ���ҵ�һ��ƥ�䡣

