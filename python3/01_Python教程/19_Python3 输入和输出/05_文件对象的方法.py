'''
文件对象的方法
本节总剩下的例子假设已经创建了一个称为 f 的文件对象。

f.read()
为了读取一个文件的内容，调用 f.read(size)， 这将读取一定数目的数据，然后作为字符串或字节对象返回。
size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负，那么该文件的所有内容都将被读取并且返回。
'''
f = open('19_Python3 输入和输出/temp/test.txt','r')
print(f.read())

'''
f.readline()
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。
f.readline() 如果返回一个空字符串，说明已经读区到最后一行。
'''
print('-' * 30)
f = open('19_Python3 输入和输出/temp/test.txt','r')

print(f.readline())
print(f.readline())

'''
f.readlines()
f.readlines() 将返回该文件中包含的所有行。
如果设置可选参数 sizehint, 则读取指定长度的字节，并且将这些字节按行分割。
'''
print('+' * 30)
f = open('19_Python3 输入和输出/temp/test.txt','r')
readStr = f.readlines()
print(readStr)
print(len(readStr))
print(len(str(readStr)))
print('-' * 30)
f = open('19_Python3 输入和输出/temp/test.txt','r')
readStr = f.readline()
print(len(readStr)) # readline() 获取到的是列表list，大小为 2
print(len(str(readStr)))
f = open('19_Python3 输入和输出/temp/test.txt','r')
print(f.readlines(35))
f = open('19_Python3 输入和输出/temp/test.txt','r')
print(f.readlines(36))

print('*' * 30)
# 另一种方式是迭代一个文件对象然后读取每行：
f = open('19_Python3 输入和输出/temp/test.txt','r')
for line in f:
    print(line, end='')


# 这个方法很简单，但是并没有提供一个很好的控制。因为两者的处理机制不同，最好不要混用。

'''
f.write()
f.write(string) 将 string 写入到文件中，然后返回写入的字符串。 
'''
f = open('19_Python3 输入和输出/temp/test2.txt','w')
f.write('This is a test\n')

# 如果要写入一些不是字符串的东西，那么将需要先进行转换：
f = open('19_Python3 输入和输出/temp/test3.txt','w')
value = ('the answer', 42)
s = str(value)
f.write(s)

print()
print('+' * 30)
'''
f.tell()
f.tell() 返回文件对象当前所处的位置，它是从文件开头开始算起的字节数。
'''
print(f.tell())

'''
f.seek()
如果要改变文件当前的位置，可以使用 f.seek(offset, from_what) 函数。
from_what 的值，如果是 0 表示开头，如果是 1 表示当前位置, 2 表示文件的结尾，例如：
seek(x, 0): 从起始位置即文件首行首字符开始移动 x 个字符
seek(x, 1): 表示从当前位置往后移动 x 个字符
seek(-x, 2): 表示从文件的结尾往前移动 x 个字符
from_what 值为默认为 0,即文件开头。下面给出一个完整的例子：
'''
f = open('19_Python3 输入和输出/temp/workfile','rb+')
r = f.write(b'0123456789abcdef')
print(r)

print(f.seek(5)) # 移动到文件的第六个字节

print(f.read(1))
print(f.seek(-3, 2)) # 移动到文件的倒数第三字节
print(f.read(1))

'''
f.close()
在文本文件中（那些打开文件的模式下没有 b 的）,只会相对于文件起始位置进行定位。
当你处理完一个文件后，调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
'''
f.close()
f.read()

# 文件对象还有其他方法，如 isatty() 和 trucate(), 但这些通常比较少用。
    


