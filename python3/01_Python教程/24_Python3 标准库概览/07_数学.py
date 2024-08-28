'''
数学
math 模块为浮点运算提供了对底层 C 函数库的访问：
'''
import math
print(math.cos(math.pi / 4))

print(math.log(1024, 2))

'''
random 提供了生成随机数的工具。
'''
import random
print(random.choice(['apple', 'pear', 'banana']))

print(random.sample(range(100), 10)) # sampling without replacement

print(random.random())      # random float

print(random.randrange(6))  # random integer chosen from range(6)