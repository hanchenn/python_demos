#布尔表达式
'''
布尔操作符：and,or ,not

布尔操作符的优先级：not>and>or
eg: a or not b and c == a or ((not b) and c)

布尔代数

数字的零值==false,任何非零值都是true
非空字符串==True，空字符串==False
非空列表==True，空列表==False

Python中的and or 都是短路的

bool类型实际上是一个特殊的整数:True+False==1
'''
def boolDemo():
    ans = input("Please input a flavor you want:[vanilla]:")
    if ans:
        flavor = ans
    else:
        flavor = "vanilla"
    print("Your flavor is:",flavor)
    
#通过将字符串处理成布尔类型来简化boolDemo(),Python 牛逼
def boolDemo2():
    flavor = input("Please input a flavor you want:[vanilla]:") or "vanilla"
    print("Your flavor is:",flavor)
    
def main():
    boolDemo2()

main()
