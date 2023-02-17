#coding=utf-8
# 斐波那契数列(Fibonacci sequence)，又称黄金分割数列，因数学家莱昂纳多·斐波那契(Leonardo Fibonacci)以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、...

# 这个数列，前两项都是数字 1，从第三项开始，每一项数字是前两项数字之和

# 数学表达式：f(n) = f(n-1)+f(n-2)

def fib(n):
    if n <=2:
        return 1
    return fib(n-1)+fib(n-2)

print fib(10)
print fib(2)

# 递归与栈的关系 递归函数原理：每一次调用都会把当前调用压入到栈里，最后按照后进先出的原则，不停返回返回 由递归程序的执行过程，我们得知递归程序的调用是一层层向下的，而返回过程则恰好相反，一层层向上。

# 换个说法：最先一次的函数调用在最后返回，而最后一次的函数调用则是最先返回。这就跟栈的“后进先出”次序是一样的。因此，在实现递归调用的时候，通常就会使用栈来保存每一次调用的现场数据：

# 当一个函数被调用的时候，系统会把调用时的现场数据压入到系统调用栈，压入栈的现场数据称为栈帧。当函数返回时，要从调用栈的栈顶取得返回地址，恢复现场，弹出栈帧，按地址返回。