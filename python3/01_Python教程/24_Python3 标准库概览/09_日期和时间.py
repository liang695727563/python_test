'''
日期和时间
datetime 模块为日期和时间处理同时提供了简单和复杂的方法。
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
该模块还支持时区处理：
'''

# dates are easily constructed and formated
from datetime import date
now = date.today()
print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)