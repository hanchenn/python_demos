# -*- coding: cp936 -*-
#Python的字典
'''
通过任意键值查找集合中值信息的过程叫映射
Python中通过字典实现映射

字典是一个键值对的集合，该集合以键为索引，同一个键信息对应一个值
eg：password = {"China":"BigCountry","Korean":"SmallCountry","France":"MediumCountry"}
注意字典是无序的。

字典的操作
1.字典初始化，通过一对大括号创建、初始化字典
2.增加一项，通过一对中括号增加一项：字典名[键] = 值
3.取值，通过键来取值：字典名[键]即可取到
4.删除字典中的一项，使用命令：del 字典名[键]
5.字典的遍历：
  5.1遍历字典的键key
    for key in 字典名.keys()
  5.2遍历字典的值value
    for value in 字典名.values()
  5.3遍历字典的项
    for item in 字典名.item()
  5.4遍历字典的key-value
    for item,value in adict.items()

判断
判断一个键是否在字典中:in 或者 not in
eg:"20141120012" in students --->true

字典的标准操作符
-,<,>,<=,>=,==!=,and,or,not

字典方法
keys() 返回一个包含字典所有key的列表
values() 返回一个包含字典所有value的列表
items() 返回一个包含所有键值的列表(列表元素是二维元组)
clear() 删除字典中的所有项目，返回None
get(key) 返回字典中key对应的值
pop(key) 删除并返回字典中key对应的值
updata(字典) 将字典中的键值添加到字典中


'''
#字典实例一：统计文件词频
'''
思路：
选用的数据结构是字典
先将各种标点符号换成空格，然后通过空格断词
字典的键为词，值为次数

步骤：
1. 断词，将所有出现的词放在一个列表中；
2.遍历列表中的词，如果此存在于字典中，就给对应的词频+1,如果不存在，就新添一个词，
词频+1（词频默认为0）

'''
import turtle

##全局变量##
#词频排列显示个数
count = 10
#单词频率数组——作为y轴数据
data = []
#单词数据——作为x轴数据
words = []
#y轴显示放大倍数——可以根据词频数量进行调节
yScale = 6
#x轴显示放大倍数——可以根据count数量进行调节
xScale = 30

####################Turtle Start#################
#从点(x1,y1)到(x2,y2)绘制线段
def drawLine(t,x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)

#在坐标(x,y)处写文字
def drawText(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)

def drawGraph(t):
    #绘制x/y轴线
    drawLine(t,0,0,360,0)
    drawLine(t,0,300,0,0)

    #x轴：坐标及描述
    for x in range(count):
        x = x+1 #向右移一位，为了不画在圆点上
        drawText(t,x*xScale-4,-20,(words[x-1]))
        drawText(t,x*xScale-4,data[x-1]*yScale+10,data[x-1])
    drawBar(t)

#绘制一个柱体
def drawRectangle(t,x,y):
    x = x*xScale
    y = y*yScale
    drawLine(t,x-5,0,x-5,y)
    drawLine(t,x-5,y,x+5,y)
    drawLine(t,x+5,y,x+5,0)
    drawLine(t,x+5,0,x-5,0)


#绘制多个柱体
def drawBar(t):
    for i in range(count):
        drawRectangle(t,i+1,data[i])

##################Turtle End###################

#对文本的每一行计算词频的函数
def processLine(line,wordCounts):
    #用空格替换标点符号
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


#替换文件中乱七八糟的符号
def replacePunctuations(line):
    for ch in line:
        if ch in " ~@#%$%^&()_-=+<>?,.:;{}[]|\'""": #有点不理解
            line = line.replace(ch,"")
    return line

def main():
    #用户输入一个文件名
    filename = raw_input("Please input a file name:")
    infile = open(filename,'r')

    #建立用于计算词频的空字典
    wordCounts = {}
    for line in infile:
        processLine(line.lower(),wordCounts)

    #从字典中获取数据对
    pairs = list(wordCounts.items())

    #列表中的数据对交换位置，数据对排序
    items = [[x,y]for (y,x) in pairs]
    items.sort()#有点不理解

    #输出count个数词频结果
    for i in range(len(items)-1,len(items)-count-1,-1):
        print(items[i][1]+"\t"+str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
    
    #根据词频结果绘制柱状图
    turtle.title("词频结果柱状图")
    turtle.setup(900,750,0,0)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(3)
    drawGraph(t)

    #调用main函数
    if __name__ == '__name__':
        main()

main()









