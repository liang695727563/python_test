'''
Python 二次方程
以下实例为通过用户输入数字，并计算二次方程：

'''
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供

# 导入 cmath(复杂数学运算) 模块
import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b**2) - (4*a*c)

# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))

# 该实例中，我们使用了 cmath(complex math) 模块的 sqrt() 方法 来计算平方根。