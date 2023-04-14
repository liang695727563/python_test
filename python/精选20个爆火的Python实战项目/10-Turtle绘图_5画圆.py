# 这个圆画的不漂亮，起始点貌似有个尾巴，这是画笔最开始从中心位置挪到设定位置时画笔移动的痕迹。
#
# 如何去除这个痕迹呢？
#
# 我们可以这样做：使用turtle提供的提笔方法penup( )，也就是先从中心点将画笔提起来，画笔在空中挪至设定位置，然后到了设定位置再将画笔落到画布上，此时就使用落笔方法turtle.pendown( )，这样我们修改上述代码如下：
# ————————————————
# 版权声明：本文为CSDN博主「安嘉门院」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_28929303/article/details/112336492

import turtle
wn = turtle.Screen()
turtle.bgcolor('black')
turtle.color('white')
turtle.circle(100)
turtle.color('red')
turtle.penup() #提起画笔
turtle.setpos(10,10)
turtle.pendown() #落下画笔
turtle.circle(100)
turtle.hideturtle() # 同时如果想画图结束时那个画笔不显示，可以使用hideturtle方法，即隐藏画笔。

wn.exitonclick()
# https://blog.csdn.net/weixin_28929303/article/details/112336492

