#coding=utf-8
# 己知数字 a，b，c 分别为 10，6，18 
# 找出 a，b，c 中最大的数字(不借助函数以及列表等方式) 
# 我们知道函数 max 可以直接获取到最大值，
# 或者可以把数字添加到列表里，通过排序也能获取到最大数字，
# 我们单纯使用 if 分支来实现

a, b, c = 10, 6, 18
if a > b:
    max_num = a
else:
    max_num = b

if max_num < c:
    max_num = c

print max_num