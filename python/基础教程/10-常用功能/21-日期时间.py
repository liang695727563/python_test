# -*- coding: UTF-8 -*-

import time;    # ����timeģ��

ticks = time.time()
print "��ǰʱ���Ϊ��", ticks

# �ӷ��ظ�������ʱ��꡷�ʽ��ʱ��Ԫ��ת����ֻҪ�����������ݸ��� localtime ֮��ĺ�����
localtime = time.localtime(time.time())
print "����ʱ��Ϊ��", localtime;

# ����Ը�������ѡȡ���ָ�ʽ��������򵥵Ļ�ȡ�ɶ���ʱ��ģʽ�ĺ�����asctime():
localtime = time.asctime(time.localtime(time.time()))
print "����ʱ��Ϊ �� ", localtime;

# ��ʽ������
# ���ǿ���ʹ�� time ģ��� strftime ��������ʽ�����ڣ�

# ��ʽ����2023-01-08 15:05:34
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# ��ʽ����Sun Jan 08 15:07:39 2023
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# ����ʽ�ַ���ת��Ϊʱ���
a = "Sun Jan 08 15:07:39 2023"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

# ��ȡĳ������
# Calendar ģ���кܹ㷺�ķ����������������������������ӡĳ�µ�������

import calendar;
cal = calendar.month(2016,1)
print "�������2016��1�·ݵ�������"
print cal;

