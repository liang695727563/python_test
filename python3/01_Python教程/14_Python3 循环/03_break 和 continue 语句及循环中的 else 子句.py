'''
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，
任何对应的循环 else 块将不执行。

continue 语句被用来告诉 Python 跳过当前循环中的当此循环，然后继续进行下一轮循环。

循环语句可以有 else 子句；它在穷尽列表(以 for 循环)或条件变为假(以 while 循环)循环终止时被执行，
但循环被 break 终止时不执行，如下查寻质数的循环例子:
'''
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # 循环中没有找到元素
         print(n, 'is a prime number')