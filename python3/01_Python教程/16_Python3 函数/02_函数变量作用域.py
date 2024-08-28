'''
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
'''

a = 4   # 全局变量

def print_func1():
    a = 17  # 局部变量
    print('in print_func a = ', a)

def print_func2():
    print('in print_func a = ', a)

print_func1()
print_func2()
print("a = ", a)