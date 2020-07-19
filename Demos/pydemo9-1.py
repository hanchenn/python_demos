# -*- coding: cp936 -*-
#图形编程、图形对象
'''
图形显示方法：
    图素法
        以图形对象为基本元素，如矩形圆形
        图形——矢量图

    像素法
        以对象为基本元素
        图像——标量图


GUI 图形用户界面

Tkinter ——Python标准GUI
Graphics——基于Tkinter扩展
Turtle——Python内置图形库


'''
#简单图形编程
#导入图形模块
import graphics
#创建图形窗口
win = graphics.GraphWin()
#关闭窗口
win.close()

'''
图形窗口：点（像素）的集合
GraphWin对象尺寸默认值，高200像素，宽200像素

点对象point
图形模块中最简单的对象
参考坐标系定位，坐标（x,y）

参考坐标系
Graphics\Tkinter
点(0,0)表示屏幕左上角
X轴正方向从左到右
Y轴正方向从上到下
默认窗口大小为200*200

form graphics import *
p1 = Point(100,100)
p1.getX()

p2 = Point(150,80)
win = GraphWin()
p1.draw(win)
p2.draw(win)

'''

'''
Turtle库：Python内置图形化模块
默认位置为（0，0）窗口中心，方向为水平向右

控制画笔绘制的方法
 pendown():放下画笔，移到指定点后继续绘制
 penup():提起画笔，用于另起一个地方绘制时使用，与pendown()配对使用
 pensize(width):设置画笔粗细

Turtle运动方法：
 forward():沿着当前方向前进指定距离
 backward():沿着当前相反方向后退指定距离
 right(angle):向右旋转angle角度
 lefg(angle):向左旋转angle角度
 goto(x,y):移动到绝对坐标（x，y）处
 setx():将当前x轴移动到指定位置
 sety():将当前y轴移动到指定位置
 setheading(angle):设置当前朝向为angle角度（0：东  90：北  180：西  270：南）
 home():设置当前画笔位置为原点，朝向东
 circle():绘制一个指定半径、角度、步骤的圆
 dot(r):绘制一个指定直径和颜色的圆点
 undo():撤销画笔最后一步动作
 speed():设置画笔的绘制速度，参数为0-10之间
 
 

'''






















