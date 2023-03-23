# coding=utf-8
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# 程序分析：可填充百位、十位、个位 的数字都是 1、2、3、4.组成所有的排列后再去掉不满足条件的排序。

n = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print i, j, k
                n+=1;
print n;
