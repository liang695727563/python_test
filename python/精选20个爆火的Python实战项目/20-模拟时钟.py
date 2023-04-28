try:
    import Tkinter
except:
    import tkinter as Tkinter

import math
import time
class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x = 150  # 中心点x坐标
        self.y = 150  # 中心点y坐标
        self.length = 50
        self.creating_all_function_trigger()

    # 触发器
    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.creating_background_()
        self.creating_sticks()
        return

    # 创建背景
    def creating_background_(self):
        self.image = Tkinter.PhotoImage(file='clock.gif')
        self.canvas.create_image(150, 150, image=self.image)
        return

    # 创建画布
    def create_canvas_for_shapes(self):
        self.canvas = Tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='yes', fill='both')
        return
    # 创建移动的线条
    def creating_sticks(self):
        self.sticks = []
        for i in range(3):
            store = self.canvas.create_line(self.x, self.y, self.x+self.length, self.y+self.length, width=2, fill='red')
            self.sticks.append(store)
            return

    # 定期刷新
    def update_class(self):
        now = time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime("%I", t))*5
        now = (hour, now.tm_min, now.tm_sec)

        # 改变坐标f
        for n, i in enumerate(now):
            x, y = self.canvas.coords(self.sticks[n])[0:2]
            cr = [x, y]
            cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
            cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
            self.canvas.coords(self.sticks[n], tuple(cr))
            return

if __name__ == '__main__':
    root = main()
    while True:
        root.update()
        root.update_idletasks()
        root.update_class()