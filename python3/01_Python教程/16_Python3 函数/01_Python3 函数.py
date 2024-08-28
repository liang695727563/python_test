'''
Python 定义函数使用 def 关键字，一般格式如下：

def  函数名（参数列表）：
    函数体
'''

# 让我们使用函数来输出"Hello World！"：
def hello():
    print('Hello World!')

hello()

# 更复杂点的应用，函数中带上参数变量:
def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)

print_welcome("Fred")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
