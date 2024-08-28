'''
Python 交换变量
以下实例通过用户输入两个变量，并相互交换：

'''
# 用户输入
x = input('输入 x 值：')
y = input('输入 y 值：')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后 x 的值为：{}'.format(x))
print('交换后 y 的值为：{}'.format(y))

# 以上实例中，我们创建了临时变量 temp ，并将 x 的值存储在 temp 变量中，接着将 y 值赋给 x，最后将 temp 赋值给 y 变量。

'''
不使用临时变量
我们也可以不创建临时变量，用一个非常优雅的方式来交换变量：
x,y = y,x

'''
#  用户输入

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 不使用临时变量
x,y = y,x

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))