'''
性能度量
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
例如。使用元组封装和拆封来交换元素看起来比使用传统的方法要诱人的多。timeit 证明了现代的方法更快一些。
'''
from  timeit import Timer
time1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(time1)

time2 = Timer('a,b= b,a', 'a=1; b=2').timeit()
print(time2)

'''
相对于 timeit 的细粒度， :mode:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。
'''