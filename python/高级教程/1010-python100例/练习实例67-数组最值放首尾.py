# coding=utf-8
# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
def inp(number):
    for i in range(9):
        number.append(int(raw_input('input a number:\n')))
    number.append(int(raw_input('input a number:\n')))

p = 0

def max_min(array):
    max = min = 0
    for i in range(1, len(array) -1):
        p = i
        if array[p] > array[max] : max = p
        elif array[p] < array[min] : min = p
    k = max
    l = min
    array[0], array[l] = array[l],array[0]
    array[9], array[k] = array[k],array[9]

def outp(number):
    for i in range(len(number)):
        print number[i]

if __name__ == '__main__':
    array = []
    inp(array)
    max_min(array)
    outp(array)

