#python的循环结构
'''
Python中for循环的格式：
for var in sequence:
    body

Python的for遍历是在sequence列表中直接进行遍历而并非拷贝之后遍历。

注意；break和continue可以用于for和while循环

else在for/while中的用法
此时的else是与for或者while语句搭配使用，
只有在循环正常结束，并非由break啥的跳出循环的时候else才会执行



'''
def forDemo():
    words = ['cat','window','defensestrate']
    for w in words[:]:
        if len(w)> 6:
            words.insert(0,w)

    print(words)

    
def forDemo2():
    n = eval(input("How many numbers?"))
    sum = 0.0
    for i in range(n):
        x = eval(input("Enter a number >>"))
        sum+=x
    print("\nThe average is",sum/n)

#使用带else的for循环做素数的判断很方便
def judgePrime():
    for n in range(2,10):
        for x in range(2,n):
            if n % x == 0 :
                print(n,"==",x,"*",n//x)
                break;
        else:
            print(n,"is a prime number")

#交互式循环求平均数示例
def calAvg1():
    sum = 0.0
    count = 0
    moredata = 'yes'
    while(moredata[0]=='y'):
        x = int(input("Please input the x:"))
        sum += x
        count = count +1
        moredata = input("There is more data to calculate?(yes/no)")

        result = sum/count;
    print("The result of sum/count is:",result)


#哨兵循环求平均数示例,即设置一个哨兵值作为循环终止的标志
def calAvg2():
    try:
        sum = 0.0
        count = 0
        xStr = input("Please input the number(empty is the ending symbol)")
        while(xStr != ""):
            sum += eval(xStr)
            count = count + 1
            xStr = input("Please input the number(empty is the ending symbol)")
        result = sum/count;
        print("The average is: ",result)
    except ZeroDivisionError:
        print("You need input something")

    except:
        print("There is something wrong...")

    finally:
        print("Ending...clean the floor...")
    
    
#Python中的文件循环，即利用循环读取文件内容
def fileLoop():
    try:
        fileName = input("What file are the numbers in?")
        infile = open(fileName,'r')
        sum = 0.0
        count = 0
        for line in infile:
            sum = sum + eval(line)
            count = count +1 
        print("\nThe average of the numbers is",sum/count)
    except:
        print("someting wrong happens, bro")
#应用readLine哨兵循环应用到文件循环读取中
def fileLoop2():
    fileName = input("Where are the fucking numbers are?")
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while(line!=""):
        for xStr in line.split(','):
            print("xStr is :",xStr)
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print("The fucking average is:",sum/count)

#Python中的死循环
def deadLoop():#只有用户输入的数据为数字类型时循环才会结束
    while True:
        try:
            x = int(input("Please input a number:"))
            break
        except ValueError:
            print("wrong number!")

#Python中没有do-while循环，但是可以通过while+break间接实现
def dowhileLoop():
    while(True):
        try:
            x = int(input("Please input a number:"))
            if x >= 0: break
        except ValueError:
            print("input the fucking number please..")
            
def main():
    dowhileLoop()


main()
