#coding=utf-8

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10);
print "读取的字符串是：", str

# 查找当前位置
position = fo.tell();   # tell() 方法告诉你文件内的当前位置
print "当前文件位置：", position

#把指针再次重新定位到文件开头
position = fo.seek(0, 0);
# seek（offset [,from]）方法改变当前文件的位置。
# Offset 变量表示要移动的字节数。From 变量指定开始移动字节的参考位置。

str = fo.read(10);
print "重新读取字符串：", str
# 关闭打开的文件
fo.close()
