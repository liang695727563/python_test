'''
Python 中的循环语句有 for 和 while。
'''
'''
while 循环
Python 中 while 语句的一般形式：

while 判断条件：
    statements
同样需要注意冒号和缩进。另外，在Python中没有 do-while 循环。

以下实例使用了 while 来计算 1 到 100 的总和：
'''
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter     
    counter += 1  
print('Sum of 1 until %d: %d' % (n,sum)) 

'''
for 语句
Python for 循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for 循环的一般格式如下：

for <variable> in <sequence>:
  <statements>
else:
 <statements>
'''

languages = ["C", "C++", "Perl", "Python"] 
for x in languages:
    print(x)

print('+' * 30)
'''
以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
'''

edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")
