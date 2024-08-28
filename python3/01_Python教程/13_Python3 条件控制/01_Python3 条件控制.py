'''
Python3 条件控制
if语句
Python条件语句是通过一条或多条语句的执行结果(True或者False)来决定执行的代码块。

Python 中 if 语句的一般形式如下所示：

if condition_1:
    statement_block_1

这种if语句只有在符合条件的时候才会执行代码块内的代码，是一种比较常见的用法。

另一种常见的用法是：

if condition_1:
    statement_block_1
else:
    statement_block_2

这种语句是一种常用的if-else语句，通常用于二分支结构的条件语句代码。

在一些时候，我们可能需要多分支的条件语句代码，可以在if-else语句中混合elif语句进行使用：

Python 中用 elif 代替了else if，所以if语句的关键字为：if – elif – else。

if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句，如果 "condition_1" 为 False，将判断 "condition_2"，如果"condition_2" 为 True 将执行 "statement_block_2" 块语句，如果 "condition_2" 为 False，将执行"statement_block_3"块语句。
'''
'''
 使用第一种常用的if语句搭配合适的条件可以实现第二种和第三种语句的全部效果，但在执行效率和代码可读性上会变得比较糟糕。
'''

'''
注意：

1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在 Python 中没有 switch – case 语句，但在python3.10中添加了用法类似的match-case语句。
'''