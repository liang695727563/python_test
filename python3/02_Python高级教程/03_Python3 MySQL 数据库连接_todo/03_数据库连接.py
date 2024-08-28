'''连接数据库前，请先确认以下事项：

您已经创建了数据库 TESTDB.
在 TESTDB 数据库中您已经创建了表 EMPLOYEE
EMPLOYEE 表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
连接数据库 TESTDB 使用的用户名为 "testuser" ，密码为 "test123",你可以可以自己设定或者直接使用 root 用户名及其密码，Mysql 数据库用户授权请使用 Grant 命令。
在你的机子上已经安装了 Python MySQLdb 模块。
如果您对 sql 语句不熟悉，可以访问我们的 SQL教程
实例：
以下实例链接 Mysql 的 TESTDB 数据库：
'''

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库连接
db.close()