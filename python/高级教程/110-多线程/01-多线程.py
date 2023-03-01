#coding=utf-8
# Python 中使用线程有两种方式：函数或者用类来包装线程对象。

# 函数式：调用 thread 模块中的 start_new_thread() 函数来产生新线程。

import thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName, time.ctime(time.time()))

# 创建两个线程
try:
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print "Error: unable to start thread"

while 1:
    pass

# 线程的结束一般依靠线程函数的自然结束；也可以在线程函数中调用 thread.exit()，他抛出 SystemExit exception，达到退出线程的目的。

