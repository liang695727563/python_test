'''
输出格式美化
Python 两种输出值的方式：表达式语句和 print() 函数。（第三种方式是使用文件对象的 write() 方法；标准输出文件可以用 sys.stdout 引用。）
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转换成字符串，可以使用 repr() 或 str() 函数来实现。
str() 函数返回一个用户易读的表达形式。
repr() 产生一个解释器易读的表达式。
'''
s = 'Hello, world.'
print(str(s))

print(repr(s))

print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# repr() 的参数可以是 Python 的任意对象
print(repr((x, y, ('spam', 'eggs'))))

print('=' * 30)
# 这里有两种方式输出一个平方与立方的表：
for x in range(1, 11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))

print('-' * 30)
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

'''
注意： 在第一个例子中，每列间的空格由 print() 添加。
这个例子展示了字符串对象的 rjust() 方法，它可以将字符串靠右，并在左边填充空格。
还有类似的方法，如 ljustU() 和 center(). 这些方法并不会写任何东西，它们仅仅返回新的字符串。
另一个方法 zfill(), 它会在数字的左边填充0.
'''
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

# str.format() 的基本使用
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
'''
括号及其里面的字符（称作格式化字段）将会被 format() 中的参数替换。
在括号中的数字用于指向传入对象在 format() 中的位置。
'''
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# 如果在 format() 中使用了关键字参数，那么它们的值会指向使用该名称的参数。
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# 位置及关键字参数可以任意的结合
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# '!a'(使用 ascii()), '!s'(使用str()) 和 '!r'(使用 repr()) 可以用于在格式化某个值之前对其进行转化：

import math
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))

# 可选项 ':' 和格式标识符可以跟着字段名。这就允许对值进行更好的格式化。
# 下面的例子将 Pi 保留到小数 点后三位：
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
# 在 ':' 后传入一个整数，可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Sjored': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

'''
如果你有一个很长的格式化字符串，而你不想将它们分开，那么在格式化时通过变量名而非位置会时很好的事情。
最简单的就是传入一个字典，然后使用方括号 '[]' 来访问键值：
'''
print('Jack: {0[Jack]:d}; Sjored: {0[Sjored]:d};\
     Dcab: {0[Dcab]:d}'.format(table)) 
# 你可以使用反斜杠 \ 来实现代码的换行连接，这通常用于一行代码过长需要分成多行时。在Python中，只有在逗号,、括号(、)、[、]、:、=这些分隔符后可以换行，其他地方不能换行。

# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
print('Jack: {Jack:d}; Sjored: {Sjored:d}; Dcab: {Dcab:d}'.format(**table))


