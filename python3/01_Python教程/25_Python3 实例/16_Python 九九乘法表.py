'''
Python 九九乘法表

'''
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()

# 通过指定 end 参数的值，可以取消在末尾输出回车符，实现不换行。