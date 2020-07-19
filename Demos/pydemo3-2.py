#math库

#random库
'''
from random import *
f = random()#生成一个0到1之间的小数
u = uniform(1,10)#在1到10之间随机生成一个小数
r = randint(1,10)#在1到10之间随机生成一个整数

randrange(0,19,2)#随机生成一个列表

ra = [0,1,2,3,4,5,6,7,8,9,]
c = choice(ra)#在列表中随机选择一个数

shuffle(ra)#随机打乱列表的顺序

sample(ra,4)#从列表中随机采样四个数据

'''
'''
以上随机操作使用的随机种子都默认是系统时钟，
可以通过seed()函数自己提供随机种子，相同的随机种子会
产生相同的伪随机序列。


'''

#使用蒙特卡洛方法进行π的计算
import math
import random
import time

def calPi(dotnum):
    times = 0

    return times

'''
def inSquare(slen,tp):
    return (tp[0]<=slen) & (tp[1]<=slen)

'''
def inCircle(slen,tp):
    distance = math.sqrt(math.pow(tp[0],2) + math.pow(tp[1],2))
    #distance = math.sqrt((tp[0])**2 + (tp[1])**2)
    return (distance<=slen)    

def main():
    num_circle=0
    
    dotnum = int(input("Please input the numbers of the dots:"))

    slen = float(input("Please input the length of the border:"))

    time.clock()

    for i in range(dotnum):
        ux = random.uniform(0,slen)
        uy = random.uniform(0,slen)
        #print("ux==",ux)
        #print("uy==",uy)
        
        if(inCircle(slen,[ux,uy])):
             num_circle+=1

        
    #print("num_circle is:",num_circle)
    print("Pi is :",num_circle/dotnum*4)
    print("This program spends ",(time.clock()),"s")

main()
