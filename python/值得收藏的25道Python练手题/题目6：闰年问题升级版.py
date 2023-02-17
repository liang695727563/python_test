# coding=utf-8

# 输入年月日，输出该日期是否是闰年，并且输出该日期是此年份的第几天

# 闰年判断条件：

# 能被 4 整除，并且不能被 100 整除
# 能被 400 整除
# 两个条件满足任意一个就为闰年
# 算法思路：

# 接收用户输入的年月日，创建保存 12 个月份天数的列表
# 根据年份判断是否是闰年，如果是把二月份设为 29 天，否则把二月份设为 28 天
# 根据月份和日期统计是当年的第几天

year = int( input("请输入年份:"))
month = int( input("请输入月份:"))
day = int( input("请输入日期:"))

date_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count_day = day
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print year, "年是闰年"
    date_list[1] =29
else:
    print year, "年时平年"
    date_list[1] =28

for i in range(month -1):
    count_day += date_list[i]

print year,"年",month,"月",day,"日是当年的第",count_day,"天"