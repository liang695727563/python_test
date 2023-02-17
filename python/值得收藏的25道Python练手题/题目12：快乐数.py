#coding=utf-8
# 在给定的数字下，该数字所有数位(digits)的平方和，得到的新数再次求所有数位的平方和，如此重复进行，最终结果必定为 1

# 比如数字：19

# 第 1 轮：(11)+(99) =1 + 81 = 82
# 第 2 轮：(88)+(22) =64 + 4 = 68
# 第 3 轮：(66)+ (88) =36 + 64 = 100
# 第 4 轮：(11) + (00) + (0*0) = 1

def sum_square(n):
    sum = 0 
    for i in str(n):
        sum += int(i) ** 2
    return sum

list1 = []
n = int(input("请输入数字："))
while sum_square(n) not in list1:
    n = sum_square(n)
    list1.append(n)

if n ==1:
    print "是快乐数"
else:
    print "不是快乐数"