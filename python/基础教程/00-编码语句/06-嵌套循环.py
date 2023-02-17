# -*- coding:UTF-8 -*-
#coding:utf-8
print "你好" 

# 嵌套输出2~100 之间的素数
i = 2
while (i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j):
        # print "{} 是素数",format(i)
        print "{} 是素数".format(i)

    i = i + 1

print "Good bye!"

#使用循环嵌套来获取 100 以内的质数
num = [];
i = 2;
for i in range(2,100):
    j = 2
    for j in range(2, i):
        if (i%j == 0):
            break
    else:
        num.append(i)
print num

# 使用嵌套循环实现*字塔的实现

i = 1
#j = 1
while i <= 9:
    if i <=5:
        print "*"*i
    elif i <= 9:
        j = i-2*(i-5)
        print "*"*j
    i+=1
else:
    print ""