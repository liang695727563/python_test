#coding=utf-8
# 中国古代文献中，曾记载过“大衍数列”，主要用于解释中国传统文化中的太极衍生原理 它的前几项是：0、2、4、8、12、18、24、32、40、50... 其规律是：偶数项，是序号平方再除 2，奇数项，是序号平方减 1 再除 2。打印大衍数列的前 100 项

for x in range(1,101):
    if x % 2 == 0 :     # 偶数
        a = int((x ** 2) / 2)
    else:   # 奇数
        a = int((x ** 2 - 1) / 2)
    print a