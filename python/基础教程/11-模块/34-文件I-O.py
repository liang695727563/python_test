# -*- coding: UTF-8 -*-
# Python 文件 I/O

# 打印到屏幕
print "Python is really a great language,", "isn't it?";

# 读取键盘输入
# Python 提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘

# raw_input() 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
str = raw_input("请输入：");
print "你输入的内容是：", str

print "————————————————————————"
# input() 函数和 raw_input() 函数基本可以互换，
# 但是 input会假设你输入是一个有效的Python表达式，并返回运算结果
str = input("Enter your input：");
print "Received input is : ", str

print "++++++++++++++++++++++++"

# 打开和关闭文件
# open函数
# 必须先用 Python 内置的 open() 函数打开一个文件，创建一个 file 对象，相关的辅助方法才可以调用它进行读写。
# 语法： file object = open(file_name [, access_mode][, buffering])

# 打开一个文件
fo = open("foo.txt", "wb")
print "文件名：", fo.name
print "是否已关闭：", fo.closed
print "访问模式：", fo.mode
# print "末尾是否强制加空格：", fo.softspace

# 关闭打开的文件
fo.close()

print "open文件："
# 打开一个文件
# fo = open("E:/python/11-模块/tmp/foo.txt", "wb")
# fo = open("/tmp/foo.txt","wb") # 相对位置为什么找不到文件
# fo = open("E:/foo.txt", "wb")
fo = open("foo.txt", "wb")
fo.write("Python is a great language.\nYeah ite great!!\n");

# 关闭打开的文件
fo.close()

print "read file:"
# read() 方法

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10);
print "读取的字符串是：", str
# 关闭打开的文件
fo.close()