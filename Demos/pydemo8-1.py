# -*- coding: cp936 -*-
'''
������̬
�����ü���������ģ��ʵ�����������

��������������ͨ�����Զ����µ���� + �Ե����ϵ�ִ��

�Զ����µ����˼·��
����һ�����㷨���Ϊһϵ��С����
�������Ϊÿ��С������ƽӿ�
��������ͨ�����㷨���Ϊ�ӿڹ����Ķ��С������ϸ���㷨
�����ģ�Ϊÿ��С�����ظ���������

һ���Զ����µ����
��һ�����������
def main():
    printIntro()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    PrintSummary(winsA,winsB)
    
�ڶ�����д������ϸ��
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
    

��������  
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

�����Ե����ϵ�ִ��

1.С��ģ����
    ֱ������
    
2.�еȹ�ģ
    �ӵײ㿪ʼ��������
    ���л����������������庯��
    ��ʵ���Ͼ����Ե����ϵĵ�Ԫ���Եķ�����

    ʹ�õ�Ԫ���Եķ����ĺô���
    1.���ڲ��͵���
    2.�������������������������



    
3.�ϴ��ģ
    �߼�������Է���


'''
#��������  
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

#�ڶ�����д������ϸ��
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
    


#��һ��
def main():
    printIntro()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    PrintSummary(winsA,winsB)

main()
