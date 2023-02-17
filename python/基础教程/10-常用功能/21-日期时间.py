# -*- coding: UTF-8 -*-

import time;    # 引入time模块

ticks = time.time()
print "当前时间戳为：", ticks

# 从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如 localtime 之类的函数。
localtime = time.localtime(time.time())
print "本地时间为：", localtime;

# 你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime(time.localtime(time.time()))
print "本地时间为 ： ", localtime;

# 格式化日期
# 我们可以使用 time 模块的 strftime 方法来格式化日期，

# 格式化成2023-01-08 15:05:34
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# 格式化成Sun Jan 08 15:07:39 2023
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sun Jan 08 15:07:39 2023"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

# 获取某月日历
# Calendar 模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：

import calendar;
cal = calendar.month(2016,1)
print "以下输出2016年1月份的日历："
print cal;

