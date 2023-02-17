# -*- coding:UTF-8 -*-
#coding=utf-8
print '你好'

count = 0
while count < 9:
    print 'The count is:', count
    count =count +1
print 'Good bye!'

''''''''''''
#coding=utf-8
#continue 和 break 用法

i=1
while i < 10:
    i +=1
    if i%2  >0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10

i = 1
while 1:        # 循环条件为1必定成立
    print i     # 输出1-10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break


""""""""""""
"""

var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = raw_input("Enter a number :")
    print "You entered: ",num

print "Cood bye!"

"""

''''''''''''''

count  = 0
while count < 5:
    print count , ' is less than 5'
    count = count +1
else:
    print count ,' is not less than 5'

''''''''
# while单行代码
flag = 1

# while (flag): print 'Given flag is really true!'

print "Good bye!"


''''''''''''

# coding=utf-8
#一个简单的使用while去除字符串前后空格的代码
str = '      W3cschool    '
#打印灭有处理前的字符串
print str

#使用循环去除字符串前的空格
while str[:1] == ' ':
    str = str[1:]
#使用循环除去字符串后的空格
while str[-1] == ' ':
    str = str[:-1]
# 打印处理后的结果
print str