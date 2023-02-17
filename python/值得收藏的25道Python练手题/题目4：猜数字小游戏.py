#coding=utf-8
#需求分析：

# 随机生成一个 100 以内的整数，共有 10 次机会开始游戏，输入猜测的数字。

# 如果猜小了，则提示：猜小了
# 如果猜大了，则提示：猜大了
# 猜对了，则提示：猜对了，并且结束游戏
# 10 次机会用完还没猜对，提示：游戏结束，没有猜到。

import random as rd;

number = rd.randint(0, 100)
for i in range(10):
    choice = int(input("请输入你要猜测的数字："))
    if choice > number:
        print "你猜大了"
    elif choice < number:
        print "你猜小了"
    else:
        print "你猜对了，真棒！"
        print "你一共用了"  , i+1 , "次机会"
        break
    print "还剩", 9-i, "次机会"
else:
    print "游戏结束，你没有猜到"
