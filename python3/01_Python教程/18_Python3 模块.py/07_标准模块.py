'''
标准模块
Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的“库参考文档”）。
有些模块直接构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没有问题。
这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Window 系统。
应该注意到这有一个特别的模块 sys,他内置在每一个 Python 解析器中。 变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串：
'''
import sys
if 'ps1' in dir(sys):
    print(True)
else:
    print(False)

# print(sys.ps1)

print('-' * 30)

''' .cmd
一下代码在cmd命令窗口中运行

import sys

sys.ps1

sys.ps2

sys.ps1 = 'c>'

print('Yuck!')
'''