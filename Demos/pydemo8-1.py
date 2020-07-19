# -*- coding: cp936 -*-
'''
计算生态
培养用计算机解决、模拟实际问题的能力

解决复杂问题可以通过：自顶向下的设计 + 自底向上的执行

自顶向下的设计思路：
步骤一：将算法表达为一系列小问题
步骤二：为每个小问题设计接口
步骤三：通过将算法表达为接口关联的多个小问题来细化算法
步骤四；为每个小问题重复上述步骤

一、自顶向下的设计
第一步：顶层设计
def main():
    printIntro()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    PrintSummary(winsA,winsB)
    
第二步：写函数的细节
def printIntro():
    print("This program simulates a game between two')
    print("There are tow players,A and B")
    print("Probability(A number between 0 and 1)is used')
    
def getInputs():
    a = eval(input("What is the prob.player A wins?"))
    b = eval(input("What is the prob.player B wins?"))
    n = eval(input("How many games to simulate?")

    return a,b,n

def simNGame(n,probA,probB):
    winA = 0
    winB = 0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA,winsB

def printSummary():
    n = winsA + winsB
    print('\nGames simulated:%d'%d)
    print('Wins for A:{0}({1:0.1%})'.format(winsA,winsA/n))
    print('Wins for B:{0}({1:0.1%})'.format(winsB,winsb/n))
    

第三步：  
def simOneGame(probA,probB):
    scoreA = 0
    scoreB = 0
    serving = 'A'
    while not gameOver(scoreA,scoreB):
        if serving == 'A':
            if random()<probA:
                scoreA = scoreA + 1
            else:
                serving = 'B'

        else:
            if random()<probB:
                scoreB = scoreB + 1
            else:
                serving = 'A'
    return scoreA,scoreB

def gameOver(a,b):
    return a==15 or b==15

二、自底向上的执行

1.小规模程序
    直接运行
    
2.中等规模
    从底层开始，逐步上升
    运行基本函数，测试整体函数
    （实际上就是自底向上的单元测试的方法）

    使用单元测试的方法的好处：
    1.便于查错和调试
    2.整个程序运行起来会更加流畅



    
3.较大规模
    高级软件测试方法


'''
#第三步：  
def simOneGame(probA,probB):
    scoreA = 0
    scoreB = 0
    serving = 'A'
    while not gameOver(scoreA,scoreB):
        if serving == 'A':
            if random()<probA:
                scoreA = scoreA + 1
            else:
                serving = 'B'

        else:
            if random()<probB:
                scoreB = scoreB + 1
            else:
                serving = 'A'
    return scoreA,scoreB

def gameOver(a,b):
    return a==15 or b==15

#第二步：写函数的细节
def printIntro():
    print("This program simulates a game between two")
    print("There are tow players,A and B")
    print("Probability(A number between 0 and 1)is used")
    
def getInputs():
    a = eval(raw_input("What is the prob.player A wins?"))
    b = eval(raw_input("What is the prob.player B wins?"))
    n = eval(raw_input("How many games to simulate?"))

    return a,b,n

def simNGames(n,probA,probB):
    winA = 0
    winB = 0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA,winsB

def printSummary():
    n = winsA + winsB
    print('\nGames simulated:%d'%d)
    print('Wins for A:{0}({1:0.1%})'.format(winsA,winsA/n))
    print('Wins for B:{0}({1:0.1%})'.format(winsB,winsb/n))
    


#第一步
def main():
    printIntro()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    PrintSummary(winsA,winsB)

main()
