"""
定义清理行为
try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。
"""
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

'''
以上例子不管 try 子句里面有没有发生异常，finally 子句都会执行。
如果一个异常在 try 子句里 （或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，
那么这个异常会在 finally 子句执行后再次被抛出。

下面是一个更加复杂的例子（在同一个 try 语句里包含 except 和 finally 子句）：
'''
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)

divide(2, 0)

divide('2', '1')
