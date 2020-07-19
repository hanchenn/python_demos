#FilePracticeDemo1
'''
程序需求：根据文件data.txt中的数据，使用turtle库来动态绘制徒刑路径

'''
import turtle
def turtleMove():
    #设置窗口信息
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800,600,0,0)
    #设置画笔
    pen = turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(5)

    #读取文件
    file = open("_turtleRoute.txt","r")
    route = []
    for line in file:
        route.append(list(map(float,line.split(","))))
    print(route)

    #动态绘制
    for i in range(len(route)):
        pen.color(route[i][3],route[i][4],route[i][5])
        pen.fd(route[i][0])
        if route[i][1]:
            pen.rt(route[i][2])
        else:
            pen.lt(route[i][2])
    pen.goto(0,0)

    
def main():
    turtleMove()


main()
