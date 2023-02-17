# coding=utf-8

import os;

# 创建目录test
os.mkdir("test")

# 删除"test"
os.rmdir("test")
# 给出当前目录
print "当前目录", os.getcwd()
# E:\python\11-模块
# 将当前目录修改为"/test"
os.chdir("/11-模块/test") ##??? 如何正确使用