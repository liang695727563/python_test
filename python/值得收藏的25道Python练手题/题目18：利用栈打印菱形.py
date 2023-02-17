# -*- coding: UTF-8 -*-

# 输入边长 n，打印对应边长的菱形

# 分析：

# 打印几行
# 每一行打印几个空格，几个星星
# 前几行打印之前加入到栈，利用栈的后进先出原则打印后几行的内容

def diamond(n):
    stack = []
    for i in range(1, 2 * n ):
        if i <= n:
            p_str = ' ' * (n-i) + '*' * (2 * i -1)
            if i != n:
                stack.append(p_str)
            print(p_str)
        else:
            print(stack.pop())

diamond(5)