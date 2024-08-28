'''
异常处理
以下例子中, 让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control + C 或者操作系统提供的方法）。
用户中断的信息会引发一个 KeyboardInterrupt 异常。
'''
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again   ")

'''
try 语句按照如下方式工作：
首先，执行 try 子句 （在关键字 try 和关键字 except 之间的语句）
如果没有异常发生，忽略 except 子句， try 子句执行后结束。
如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个 except 子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个 except 子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如：

except (RuntimeError, TypeError, NameError)
    pass

最后一个 except 子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，
然后再次把异常抛出。
'''
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unecpected error:", sys.exc_info()[0])
    raise

'''
try except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须在所有的 except 子句之后。
这个子句 将在 try 子句没有发生任何异常的时候执行。
'''
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close

'''
使用 else 子句不把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、而 except 又没有捕获的异常。
异常处理并不仅仅处理那些直接发生在 try 子句的中的异常，而且还能处理子句中调用函数（甚至间接调用的函数）里抛出的异常。
'''
def this_fails():
    x =/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handing run-time error: ', err)

