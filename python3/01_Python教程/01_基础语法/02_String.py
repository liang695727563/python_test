str = 'W3Cschool'

print(str)                  # 输出字符串
print(str[0:-1])            # 输出第一个到倒数第二个的所有字符
print(str[0])               # 输出字符串第一个字符
print(str[2:5])             # 输出从第三个开始到第五个的字符
print(str[2:])              # 输出从第三个开始后的所有字符
print(str[1:5:2])           # 输出从第一个开始到第五个且每隔两个的字符
print(str * 2)              # 输出字符串两次
print(str + '你好')         # 链接字符串

print('------------------------------')

print('hello\nW3Cschool')       # 使用反斜杠(\)+n 转义特殊字符
print(r'hello\nW3Cschool')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义