'''
Python 获取昨天日期
以下代码通过导入 datetime 模块来获取昨天的日期：

'''
# 引入 datetime 模块
import datetime
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

# 输出
print(getYesterday())