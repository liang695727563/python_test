import turtle
wn = turtle.Screen()
turtle.bgcolor('black')
turtle.color('white')
totalTimes = 8
for i in range(totalTimes):
    turtle.left(45)
    turtle.forward(100)

turtle.bgcolor('white')
turtle.color('red')
for i in range(180):
    turtle.left(2)
    turtle.forward(2)

turtle.bgcolor('red')
turtle.color('yellow')
turtle.circle(100)
wn.exitonclick()

# https://blog.csdn.net/weixin_28929303/article/details/112336492
