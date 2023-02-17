# coding=utf-8

# 通过创建一个新的异常类，程序可以命名它们自己的异常。
# 异常应该是典型的继承自 Exception 类，通过直接或间接的方式。
# 用户自定义异常 基类为 RuntimeError
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

# 触发该自定义异常
try:
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.args
print "自定义异常展示完毕"


