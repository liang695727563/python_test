# print 输出
print("Hello, World!") #"Hello,World!"是一个字符串变量
str = "Hello,World!"
print(str) #上一种helloworld的另一种写法

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：

x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()

print("***********")
print( x, end="\n" )
print( y, end=" " )