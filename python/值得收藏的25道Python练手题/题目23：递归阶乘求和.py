#coding=utf-8
# 一个正整数的阶乘(factorial)是所有小于及等于该数的正整数之积，并且 0 的阶乘为 1

# 如 5!=12345 计算 1!+2!+3!+4!+5!+…+10! 数学表达式：f(n) = n*f(n-1)：

def factor(n):
    if n < 2:
        return 1
    return n * factor(n -1)

s_sum = 0 
for i in range(1, 11):
    s_sum += factor(i)
print s_sum