
#coding=utf-8
# 水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number）

# 水仙花数是指一个 3 位数，它的每个位上的数字的 3 次幂之和等于它本身。例如：1^3 + 5^3+ 3^3 = 153。


for i in range(100,1000):
    i1 = i // 100       # 取百位数字 123//100=1
    i2 = i // 10 % 10   # 取十位数字 123//10=12 12%10 =2
    i3 = i % 10         # 取个位数字 123%10=3

    if i1 ** 3 + i2 ** 3 + i3 ** 3 == i:
        print  i,"是水仙花数"


# https://mp.weixin.qq.com/s/9RdeRVggEsutTLzcuHS5Qg