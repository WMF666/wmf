# 每次运行 树的形状是随机的
import turtle as T
import random
import time

# 画樱花的躯干
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 白
            else:
                t.color('purple') 
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('purple') 
            t.pensize(branch / 2)
        else:
            t.color('sienna')  
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 增加可选的花瓣颜色
def Petal(m, t, petal_color='purple'):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color(petal_color)  # 使用传入的花瓣颜色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(10, 0)  # 提高绘图速度
w.screensize(bg='wheat')  # 背景色
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 画樱花的躯干
Tree(60, t)
# 掉落的花瓣，使用自定义颜色
Petal(200, t, petal_color='purple')  # 可自定义花瓣颜色
w.exitonclick()
T.done()
