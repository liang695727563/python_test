#coding=utf-8
# 题目： 求0-7所能组成的奇数个数。
if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2, 9):
        print sum
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print 'sum = %d' % sum