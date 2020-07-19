#计算三角形周长
import math
def isTriangle(p1,p2,p3):
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    x3 = p3[0]
    y3 = p3[1]

    return (x1-x3)*(y2-y3) != (y1-y3)*(x2-x3)

def calDistance(p1,p2):
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
def calTriangleBorder():
    
    p1  = eval(input("Please input the Point1 (x1,y1)"))
    #print(type(p1)):tuple
    p2  = eval(input("Please input the Point1 (x2,y2)"))
    p3  = eval(input("Please input the Point1 (x3,y3)"))
    
    if isTriangle(p1,p2,p3):
        result = calDistance(p1,p2)+calDistance(p2,p3)+calDistance(p1,p3)
        print("The result is:",result)
        return result
    else:
        print("There is no fucking Triangle!!!")
        return None

def main():
    calTriangleBorder()

main()
