'''
旧式字符串格式化
% 操作符也可以实现字符串格式化。它将左边的参数作为类似 sprintf() 式的格式化字符串，
而将右边的代入，然后返回格式化后的字符串。
'''
import math
print('The value of PI is approximately %5.3f.' % math.pi)

'''
应为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。
但是因为这种旧式的格式化最终会从该语言中移除，应该更多的使用 str.format().
'''