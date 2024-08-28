'''
Python if 语句
以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：

'''
# 用户输入数字

num = float(input('输入一个数字：'))
if num > 0:
    print('正数')
elif num == 0:
    print('零')
else:
    print('负数')

# 我们可以用内嵌 if 语句来实现：

# 内嵌 if 语句
num = float(input('输入一个数字：'))
if num >= 0:
    if num == 0:
        print('零')
    else:
        print('正数')
else:
    print('负数')