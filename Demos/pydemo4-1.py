#Python 的控制结构
'''
Python中字符或者字符串的比较是按照字典顺序进行的。

布尔值的真以True,False表示。


'''

#demo解二次方程
import math
#接收一个三个元素的元组，返回两个元素的解集元组
def calEquation(params):
    a = params[0]
    b = params[1]
    c = params[2]

    derta = math.sqrt(b**2-4*a*c)
    
    if(derta>=0):
        root1 = ((-b)+derta)/(2*a)
        root2 = ((-b)-derta)/(2*a)
    else:
        print("No real roots!")

    return (root1,root2)

def main():

    params = eval(input("Please input the params of the equation in order:"))

    result = calEquation(params)

    print("Root1 = ",result[0])
    print("Root2 = ",result[1])
    print("Root3 = ",result[2])
    print("Done!")


main()
