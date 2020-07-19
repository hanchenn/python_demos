# -*- coding: cp936 -*-
#Python���ֵ�
'''
ͨ�������ֵ���Ҽ�����ֵ��Ϣ�Ĺ��̽�ӳ��
Python��ͨ���ֵ�ʵ��ӳ��

�ֵ���һ����ֵ�Եļ��ϣ��ü����Լ�Ϊ������ͬһ������Ϣ��Ӧһ��ֵ
eg��password = {"China":"BigCountry","Korean":"SmallCountry","France":"MediumCountry"}
ע���ֵ�������ġ�

�ֵ�Ĳ���
1.�ֵ��ʼ����ͨ��һ�Դ����Ŵ�������ʼ���ֵ�
2.����һ�ͨ��һ������������һ��ֵ���[��] = ֵ
3.ȡֵ��ͨ������ȡֵ���ֵ���[��]����ȡ��
4.ɾ���ֵ��е�һ�ʹ�����del �ֵ���[��]
5.�ֵ�ı�����
  5.1�����ֵ�ļ�key
    for key in �ֵ���.keys()
  5.2�����ֵ��ֵvalue
    for value in �ֵ���.values()
  5.3�����ֵ����
    for item in �ֵ���.item()
  5.4�����ֵ��key-value
    for item,value in adict.items()

�ж�
�ж�һ�����Ƿ����ֵ���:in ���� not in
eg:"20141120012" in students --->true

�ֵ�ı�׼������
-,<,>,<=,>=,==!=,and,or,not

�ֵ䷽��
keys() ����һ�������ֵ�����key���б�
values() ����һ�������ֵ�����value���б�
items() ����һ���������м�ֵ���б�(�б�Ԫ���Ƕ�άԪ��)
clear() ɾ���ֵ��е�������Ŀ������None
get(key) �����ֵ���key��Ӧ��ֵ
pop(key) ɾ���������ֵ���key��Ӧ��ֵ
updata(�ֵ�) ���ֵ��еļ�ֵ��ӵ��ֵ���


'''
#�ֵ�ʵ��һ��ͳ���ļ���Ƶ
'''
˼·��
ѡ�õ����ݽṹ���ֵ�
�Ƚ����ֱ����Ż��ɿո�Ȼ��ͨ���ո�ϴ�
�ֵ�ļ�Ϊ�ʣ�ֵΪ����

���裺
1. �ϴʣ������г��ֵĴʷ���һ���б��У�
2.�����б��еĴʣ�����˴������ֵ��У��͸���Ӧ�Ĵ�Ƶ+1,��������ڣ�������һ���ʣ�
��Ƶ+1����ƵĬ��Ϊ0��

'''
import turtle

##ȫ�ֱ���##
#��Ƶ������ʾ����
count = 10
#����Ƶ�����顪����Ϊy������
data = []
#�������ݡ�����Ϊx������
words = []
#y����ʾ�Ŵ����������Ը��ݴ�Ƶ�������е���
yScale = 6
#x����ʾ�Ŵ����������Ը���count�������е���
xScale = 30

####################Turtle Start#################
#�ӵ�(x1,y1)��(x2,y2)�����߶�
def drawLine(t,x1,y1,x2,y2):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)

#������(x,y)��д����
def drawText(t,x,y,text):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text)

def drawGraph(t):
    #����x/y����
    drawLine(t,0,0,360,0)
    drawLine(t,0,300,0,0)

    #x�᣺���꼰����
    for x in range(count):
        x = x+1 #������һλ��Ϊ�˲�����Բ����
        drawText(t,x*xScale-4,-20,(words[x-1]))
        drawText(t,x*xScale-4,data[x-1]*yScale+10,data[x-1])
    drawBar(t)

#����һ������
def drawRectangle(t,x,y):
    x = x*xScale
    y = y*yScale
    drawLine(t,x-5,0,x-5,y)
    drawLine(t,x-5,y,x+5,y)
    drawLine(t,x+5,y,x+5,0)
    drawLine(t,x+5,0,x-5,0)


#���ƶ������
def drawBar(t):
    for i in range(count):
        drawRectangle(t,i+1,data[i])

##################Turtle End###################

#���ı���ÿһ�м����Ƶ�ĺ���
def processLine(line,wordCounts):
    #�ÿո��滻������
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


#�滻�ļ������߰���ķ���
def replacePunctuations(line):
    for ch in line:
        if ch in " ~@#%$%^&()_-=+<>?,.:;{}[]|\'""": #�е㲻���
            line = line.replace(ch,"")
    return line

def main():
    #�û�����һ���ļ���
    filename = raw_input("Please input a file name:")
    infile = open(filename,'r')

    #�������ڼ����Ƶ�Ŀ��ֵ�
    wordCounts = {}
    for line in infile:
        processLine(line.lower(),wordCounts)

    #���ֵ��л�ȡ���ݶ�
    pairs = list(wordCounts.items())

    #�б��е����ݶԽ���λ�ã����ݶ�����
    items = [[x,y]for (y,x) in pairs]
    items.sort()#�е㲻���

    #���count������Ƶ���
    for i in range(len(items)-1,len(items)-count-1,-1):
        print(items[i][1]+"\t"+str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
    
    #���ݴ�Ƶ���������״ͼ
    turtle.title("��Ƶ�����״ͼ")
    turtle.setup(900,750,0,0)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(3)
    drawGraph(t)

    #����main����
    if __name__ == '__name__':
        main()

main()









