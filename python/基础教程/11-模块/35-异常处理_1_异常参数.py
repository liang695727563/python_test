# -*- coding:utf-8 -*-

# 异常的参数
# 一个异常可以带上参数，可作为输出的异常信息参数

# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "The argument does not contain numbers\n", Argument

# 调用函数
temp_convert("xyz")
print "Argument end"

# 触发异常
# 我们可以使用raise 语句自己触发异常

# 定义一个异常
def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行

# 注意：为了能够捕获异常，"except"语句必须有用相同的异常来抛出类对象或者字符串。
# 例如要捕获上述异常，”except“语句如下：
try:
    print "Business Logic here..."
    functionName("-2")
    # functionName(0)
except "Invalid level!":
    print "Exception handling here..."
else:
    print "Rest of the code here..."