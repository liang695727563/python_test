#coding=utf-8
# 什么是因子？因子就是所有可以整除这个数的数字，包括 1 但不包括这个数自身。比如 8 的因子有 1，2，4

# 什么是完数？一个数如果恰好等于它的因子之和，这个数就称为“完数”，打印输出 1000 以内的完数，例如 6=1+2+3，6 就是“完数

def factor_sum(n):
    s_sum = 0
    for i in range(1, n):
        if n % i == 0:
            s_sum += i 
    return s_sum

for j in range(1, 1000):
    if j == factor_sum(j):
        print j