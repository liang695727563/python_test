'''
在其他语言（比如说经典的C语言）中有一种多分支条件判断语句，
可以进行模式匹配（通俗的讲，就是将传入的内容跟多个已存在的样例进行比较，
找到相同的案例并按照该案例的代码进行处理，如果没有相同案例就按默认案例进行处理，
可以查看其他编程语言的条件语句的Switch相关部分内容进行比较参考）。
在python3.10中也引入了这样的新特性。

match-case语句的结构一般如下所示：

match variable: #这里的variable是需要判断的内容
    case ["quit"]: 
        statement_block_1 # 对应案例的执行代码，当variable="quit"时执行statement_block_1
    case ["go", direction]: 
        statement_block_2
    case ["drop", *objects]: 
        statement_block_3
    ... # 其他的case语句
    case _: #如果上面的case语句没有命中，则执行这个代码块，类似于Switch的default
        statement_block_default
'''
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"


'''
 上述代码等价于：
'''

def http_error(status):
    if status == 400:
        return "Bad request"
    elif status == 404:
        return "Not found"
    elif status == 418:
        return "I'm a teapot"
    else:
        return "Something's wrong with the Internet"