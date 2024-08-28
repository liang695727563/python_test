# Python 中的字符串 str 用单引号(' ')或双引号 (" ") 括起来，同时使用反斜杠 (\) 转义特殊字符。

s = 'Yes,he doesn\'t'
print(s, type(s), len(s))

# 如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('c:\some\name')
print(r'c:\some\name')

print('str' + 'ing', 'my'*3) #另外，反斜杠可以作为续行符，表示下一行是上一行的延续。还可以使用"""..."""或者'''...'''跨越多行。字符串可以使用 + 运算符串连接在一起，或者用 * 运算符重复
print('*' * 18)

'''
Python 中的字符串有两种索引方式，第一种是从左往右，从 0 开始依次增加；第二种是从右往左，从 -1 开始依次减少。

注意，没有单独的字符类型，一个字符就是长度为 1 的字符串。
'''
word = 'Python'
print(word[0], word[5])

print(word[-1], word[-6])

print('-' * 20)
'''
还可以对字符串进行切片，获取一段子串。用冒号分隔两个索引，形式为变量[头下标:尾下标]。

截取的范围是前闭后开的（头下标取，尾下标不取），并且两个索引都可以省略：
'''
word = 'ilovepython'
print(word[1:5])
print(word[:])
print(word[5:])
print(word[-10:-6])
'''
与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如 word[0] = 'm' 会导致错误。

注意：

1、反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。
2、字符串可以用 + 运算符连接在一起，用 * 运算符重复。
3、Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
4、Python 中的字符串不能改变。
'''