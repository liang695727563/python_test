'''
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

from modname import name1[, name2[, ... nameN]
'''

# 例如，要导入模块 fibo 的 fib 函数，使用如下语句：
from fibo import fib, fib2
print(fib(500))
# 这个声明不会把整个 fibo 模块导入到当前的命名空间中，它只会将 fibo 里的 fib 函数引入进来。


'''
from ... import * 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

from modname import *
这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多的使用。
'''