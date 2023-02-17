# -*- coding: UTF-8 -*-
# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句

# 导入模块
import aname;

# 现在可以掉用模块里包含的函数
aname.print_func("Zara")

# From...import 语句
# 从模块中导入一个指定部分到当前命名空间中
# 如：from modname import name1[, name2[, ... nameN]]
# from fib import fibonacci
# 这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将fib里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。

# From…import* 语句
# from modname import *
# 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。