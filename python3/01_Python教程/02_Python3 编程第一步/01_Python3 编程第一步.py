# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1         # 复合赋值：变量 a 和 b 同时得到新值 0 和 1。
while b < 10:
    print(b)
    a, b = b, a+b   # 复合赋值的方法：等价于 c = a，a = b，b = b + c。


i = 1024 * 1024
print('i 的值为：', i)  # 输出变量值


# 关键字 end 可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

# 两个元素的总和确定了下一个数
a, b = 0, 1
while b <1024:
    print(b, end = ',')
    a, b = b, a + b

print("")
# 使用 if 条件控制  
age = int(input('请输入你家狗狗的年龄：'))
print("")
if age < 0:
    print("请输入正确的年龄：")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄：", human)
# 退出提示，本地环境下可以使用这样的退出提示使代码更易用
input("点击 enter 键退出")