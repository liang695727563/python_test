#coding=utf-8
# 写法 1：切片方式
str = raw_input("请输入字符串：")
# str = input("请输入字符串：")  # 为什么输入的字符串变成变量了？

print str
print (str[::-1])

# 写法 2：循环转换
str = raw_input("请输入字符串:")
print str
list = []
for x in range(len(str) -1, -1, -1):
    list.append(str[x])
print ''.join(list)
