# coding=utf-8

# 异常处理代码执行说明
# This is note foe exception

try:
    code    # 需要判断是否会抛出异常的代码，如果没有异常处理，python会直接停止执行程序

except: # 这里会捕捉到上面代码中的异常，并根据异常抛出异常处理信息
# except ExceptinoName arg： # 同时也可以接受异常名称和参数，针对不同形式的异常处理

    code    # 这里执行异常处理的相关代码，打印输出等

else:   # 如果没有异常则执行else

    code    # try部分被正常执行后执行的代码

finally：
    code    # 退出try语句块会执行的程序

# 函数中做异常检测
def try_exception(num):
    try:
        return int(num)
    except ValueError, arg:
        print arg, "is not a mumber"
    else:
        print "this is a number inputs"

try_exception('xxx')

# 输出异常值
Invalide literal for int() with base 10: 'xxx' is not a number