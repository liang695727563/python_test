'''
操作符	描述
<	小于
<=	小于或等于
>	大于
>=	大于或等于
==	等于，比较对象是否相等
!=	不等于

 只要返回结果为布尔型（true或者false）的，都可以作为if的条件，
 所以在之前的集合等内容中涉及到的判断元素是否在集合中的​in​和​not in​，都可以作为if的条件。
'''

thisset = set(("Google", "W3Cschool", "Taobao"))
if "W3Cschool" in thisset:
    print("该元素在列表中")
if "baidu" not in thisset:
    print("该元素不在列表中")


print('-' * 30)

# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("猜数字!")
while guess != number:
    guess = int(input("请输入你要猜的数字"))
    if guess == number:
        print("你猜中了，真厉害！")
    elif guess < number:
        print("猜小了，再猜猜？")
    elif guess > number:
        print("猜大了，在猜猜？")