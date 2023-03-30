print('\n'.join([''.join([('lovelovelove'[(x-y)%12]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

# ————————————————
# 版权声明：本文为CSDN博主「灰小猿」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_44985880/article/details/106989809