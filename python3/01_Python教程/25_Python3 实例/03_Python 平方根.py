'''
Python 平方根
平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。

以下实例为通过用户输入一个数字，并计算这个数字的平方根：
'''
num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num, num_sqrt))

'''
在该实例中，我们通过用户输入一个数字，并使用指数运算符 ** 来计算改数的平方根。

该程序只适用于正数。负数和复数可以使用以下的方式：
'''

# 计算实数和复数平方根
# 导入复数数学模块
import cmath

num = int(input('请输入一个数字：'))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))

# 该实例中，我们使用了 cmath(complex math) 模块的 sqrt() 方法。