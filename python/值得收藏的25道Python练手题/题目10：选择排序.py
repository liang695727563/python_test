# coding=utf-8
# 基本思想：从未排序的序列中找到一个最小的元素，放到第一位，再从剩余未排序的序列中找到最小的元素，放到第二位，依此类推，直到所有元素都排序完毕

import random as rd

sec_list = [rd.randint(1,100) for i in range(8)]

length = len(sec_list)
print "未排序的列表为：",sec_list

for i in range(length -1):
    min_index = i
    for j in range(i +1,length):
        if sec_list[min_index] > sec_list[j]:
            min_index = j 
    sec_list[min_index], sec_list[i] = sec_list[i], sec_list[min_index]
    print "第",i+1,"轮排好序是:",sec_list
print "最终排好序的列表为：",sec_list