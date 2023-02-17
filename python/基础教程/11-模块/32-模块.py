# _*_ coding: UTF-8 _*_
# 命名空间和作用域
'''
 global VarName 的表达式会告诉 Python， VarName 是一个全局变量，
 这样 Python 就不会在局部命名空间里寻找这个变量了。

 例如，我们在全局命名空间里定义一个变量 money。我们再在函数内给变量 money 赋值，
 然后 Python 会假定 money 是一个局部变量。然而，我们并没有在访问前声明一个局部变量 money，
 结果就是会出现一个 UnboundLocalError 的错误。取消 global 语句的注释就能解决这个问题。
'''
Money = 2000
def AddMoney():
    # 想改正代码就取消以下注释：
    global Money
    Money = Money + 1

print Money;
AddMoney();
print Money

# dir() 函数 一个排好序的字符串列表，内容是一个模块里定义过的名字。
# 返回的列表容纳了在一个模块里定义的所有模块，变量和函数，如：
# 导入内置math模块
import math

content = dir(math);
print content

# 在这里，特殊字符串变量 __name__ 指向模块的名字，__file__ 指向该模块的导入文件名
print math.__name__
# print math.__file__

print "------------------------------------"
# globals() 和 locals() 函数
# print global()
print "locals():",locals()

# reload() 函数
# 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。

# 因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。
print '++++++++++++++++++++++++++'
reload(math) # reload() 中要直接放模块的名字，而不是一个字符串形式比如想要重载hello模块，如 reload(hello)
print reload(math)




