'''
有一些字符因为在python中已经被定义为一些操作（比如单引号和双引号被用来引用字符串），
而这些符号我们可能在字符串中需要使用到。为了能够使用这些特殊字符，可以用反斜杠 \ 转义字符（同样地，反斜杠也可以用来转义反斜杠）
'''

print("line1\
    line2\
    line3")   # \(在行尾时),续行符

print("\\")     # 反斜杠符号	
print('\'')     # 单引号
print("\"")     # 双引号

print("\a")     # 响铃

print("hello \b world") # \b  退格(Backspace)
print('\000')  # 空

print('\n')  # 换行

print("hello \v world") # 纵向制表符	
print("hello \t world") # 横向制表符	

# 回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
print("Hello\rWorld!") 
print('google w3cschool taobao\r123456')

print("Hello \f World!") # 	换页

print('-' * 30)

print("\110\145\154\154\157\40\127\157\162\154\144\41") # \yyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21") # \xyy	十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行

# \other  其它的字符以普通格式输出	