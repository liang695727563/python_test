#coding=utf-8

# 无异常情况
try:
    fh = open("testfile","w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "Error: can\'t find file or read data"
else:
    print "Written content in the file successfully"
    fh.close()

print "Good bey"

# 将以上文件修改为只读，会报异常

# 使用except 而不带任何异常类型， 
# try-except语句捕获所有发生的异常。但这不是一个很好的方式，我们不能通过该程序识别出具体的异常信息。因为它捕获所有的异常

# try-finally 语句无论是否发生异常都将执行最后的代码。

'''
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print "finally-Error: can\'t find file or read data"

print "finally end"
# finally 块中的所有语句执行后，异常被再次提出，并执行except 快代码
'''

