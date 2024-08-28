'''
最后，一个较不常用的功能是可以让函数调用可变个数的参数。

这些参数被包装进一个元组(查看元组和序列)。

在这些可变个数的参数之前，可以有零到多个普通的参数:
'''
def arithmetic_mean(*args):
    if len(args) == 0 :
        return 0
    else:
        sum = 0
        for x in args:
            sum += x
        return sum / len(args)

print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))
print(arithmetic_mean())