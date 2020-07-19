import turtle

def drawSnake(rad,angle,len,neckrad):
    colors = ["red","yellow","black","brown","purple"]
    for i in range(len):
        turtle.circle(rad,angle)#turtle.circle(p1,p2):p1为circle的半径，p2位画笔划过的弧度
        turtle.circle(-rad,angle)
        turtle.pencolor(colors[i-1])
    
    turtle.circle(rad,angle/2)
    turtle.fd(rad)#turtle.fd(p):p为所画直线的长度
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
    

def main():
    turtle.setup(1300,800,0,0)#设置绘图的启动窗口
    pensize = 30
    turtle.pensize(pensize)#设置画笔宽度
    turtle.pencolor("blue")#设置画笔颜色
    turtle.seth(-40)#设置基准角度，否则画出的蛇是斜着的
    drawSnake(40,80,5,pensize/2)
    
    
    
main()

#Python引用外部库
'''
使用关键字import导入外部库

turtle库，Python中常用的绘制图像库

'''

#Python引用外部库函数
'''
有两种使用方式：
1. import 库名

    库名.函数名

2. from 库名 import 函数名
   from 库名 import *

   函数名直接使用

   

'''


#Python中的函数
'''
通过使用def关键字定义自定义函数

def定义的函数未经调用不会运行





'''
