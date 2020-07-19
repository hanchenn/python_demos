#函数实例分析
'''
Turtle的坐标原点是屏幕中心

'''
import turtle
#使用turtle库画个五角星
def drawStar():
    p = turtle.Turtle()
    p.speed(4)
    p.pensize(5)
    p.color("black","yellow")
    #p.fillcolor("red")
    p.begin_fill()
    for i in range(5):
        p.forward(200)
        p.right(144)
    p.end_fill()

def main():
    drawStar()

main()
