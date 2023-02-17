#coding=utf-8
# 游戏开始，初始状态下用户和电脑都有 100 分，赢一局+10 分，输一局-10 分。

# 当用户为 0 分时，游戏结束，提示游戏结束，比赛输了

# 当用户为 200 分时，游戏结束，提示游戏结束，赢得比赛、每轮比赛都输出当前的分数

# 1 代表剪刀 2 代表石头 3 代表布

import random as rd
print '=' * 30
print ' ' * 20, '剪刀石头布游戏'
print '1代表剪刀 2 代表石头 3代表布'

game_info = {1: "剪刀", 2: "石头", 3: "布"}
score = 100

while True:
    robots_choice = rd.randint(1, 3)
    user_choice = input("请出拳")
    if user_choice not in {1,2,3}:
        print "出拳错误,请重新出拳"
        continue
    user_choice = int(user_choice)
    print "*" * 30
    print "电脑出",game_info[robots_choice]
    print "你出",game_info[user_choice]
    print '*' * 60
    if user_choice ==1 and robots_choice ==3 \
        or user_choice ==2 and robots_choice ==1 \
            or user_choice == 3 and robots_choice ==2:
        score +=10
        print '你赢得本轮游戏，当前分数为',score
    elif user_choice == robots_choice:
        print "本轮游戏平局，当前分数为", score
    else:
        score -=10
        print '你输了本轮游戏，当前分数', score
    if score >= 200:
        print '你赢了本轮游戏，当前分数',score
        break
    elif score <= 0:
        print '游戏结束，你输了'
        break