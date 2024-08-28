'''
Python 计算每个月天数
以下代码通过导入 calendar 模块来计算每个月的天数：

'''
import calendar
monthRange = calendar.monthrange(2013, 6)
print(monthRange)
'''
输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
以上实例输出的意思为2013年 6月份的第一天是星期六，该月共有 30 天。
'''

