#coding=utf-8
# Python ��ʹ���߳������ַ�ʽ������������������װ�̶߳���

# ����ʽ������ thread ģ���е� start_new_thread() �������������̡߳�

import thread
import time

# Ϊ�̶߳���һ������
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName, time.ctime(time.time()))

# ���������߳�
try:
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print "Error: unable to start thread"

while 1:
    pass

# �̵߳Ľ���һ�������̺߳�������Ȼ������Ҳ�������̺߳����е��� thread.exit()�����׳� SystemExit exception���ﵽ�˳��̵߳�Ŀ�ġ�

