# Python 比较运算符
# 所有比较运算符返回 1 表示真，返回 0 表示假。这分别与特殊的变量 True 和 False 等价。注意：True和False的首字母为大写。
a = 21
b = 10 
c = 0

if (a == b):
    print("a 等于 b")
else:
    print("a 不等于 b")

if ( a != b ):
    print ("a 不等于 b")
else:
    print ("a 等于 b")

if ( a < b ):
    print ("a 小于 b")
else:
    print ("a 大于等于 b")

if ( a > b ):
    print ("a 大于 b")
else:
    print ("a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5;
b = 20;
if ( a <= b ):
    print ("a 小于等于 b")
else:
    print ("a 大于  b")

if ( a >= b ):
    print ("a 大于等于 b")
else:
    print ("a 小于 b")