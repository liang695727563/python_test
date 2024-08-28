'''
Python 函数使用 return 语句返回函数值，可以将函数作为一个值赋值给指定变量：
'''
def return_sum(x,y):
    c = x + y
    return c

res = return_sum(4, 5)
print(res)

print('-' * 30)
# 你也可以让函数返回空值：
def empty_return(x,y):
    c = x + y
    return


res = empty_return(4,5)
print(res)
