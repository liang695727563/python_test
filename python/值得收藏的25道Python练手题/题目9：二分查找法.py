#coding=utf-8

# 二分法适用情况

# 必须是有序的序列。
# 对数据量大小有要求。
# 数据量太小不适合二分查找，与直接遍历相比效率提升不明显。
# 数据量太大也不适合用二分查找，因为数组需要连续的存储空间，若数据量太大，往往找不到存储如此大规模数据的连续内存空间

# 算法思路：

# 假设有一个有序列表：[5,7,11,22,27,33,39,52,58]

# 请问数字 11 是否在此列表中，如果在它的索引值为多少？

# 首先我们取有序列表的中间位置 27 和 11 进行比较 我们发现 11 是小于 27 的
# 所以我们排除 27 右边的数字，保留列表为：[5,7,11,22]
# 接着我们取 [5,7,11,22] 位置中间的 7 和 11 比较 发现 11 是大于 7 的 所以我们排除 7 左边的数字，保留列表为：[11,22]
# 最后我们取 11 和 22 的中间位置
# 刚好到了 11 这时候就可以返回 11 的索引值了，如果没有找到就提示不存在

# 第1种 纯算法的方式
arr_list = [5,7, 11, 22, 27, 33, 39, 52, 58]
number =11
count = 0
left = 0
right = len(arr_list) - 1
while left <= right:
    middle = (left + right)//2
    count += 1
    if number > arr_list[middle]:
        left = middle +1
    elif number < arr_list[middle]:
        right = middle -1
    else:
        print "数字",number, "已找到，索引值为", middle
        break
else:
    print "数字",number, "没有找到"
print "一共用了",count,"次查找"

print "#"*30

# 第2种 递归函数的方式
arr_list = [5,7, 11, 22, 27, 33, 39, 52, 58]

def binary_search(number,left,right):
    if left <= right:
        middle = (left + right) // 2
        if number < arr_list[middle]:
            right = middle -1
        elif number > arr_list[middle]:
            left = middle +1
        else:
            return middle
        return binary_search(number,left,right)
    else:
        return -1

print binary_search(11,0,len(arr_list)-1)