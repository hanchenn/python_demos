#Python的异常处理
'''
Python 使用try...except...进行异常处理，可以使程序不因运行错误而崩溃

try:
    <body>
except <ErrorType1>:
    <handler1>
except <ErrorType2>:
    <handler2>
except <ErrorType3>:
    <handler3>
except:
    <handler0>

else:
    <process_else>
finally:
    <process_finally>

最后一个except是发生异常了，但是并不是预料之内的异常执行

else和finally语句是可选的
else：如果无异常产生，执行else语句；
finally；不论异常是否发生，finally后的子句都会执行。常用语一些收尾操作


try...except可以捕捉任何类型的错误

常见的异常还有：
NameError
SyntaxError


'''

def trydemo():
    try:
        num1,num2 = eval(input("Please input two numbers,separated by a comma:"))
        result = num1/num2

    #除数为0异常
    except ZeroDivisionError:
        print("Division by zero!")
    #段错误异常（即两数分隔没用逗号）
    except SyntaxError:
        print("Where is the fucking comma?...")

    except:
        print("Something wrong in the imput")

    else:
        print("No exceptions,the result is:",result)

    finally:
        print("executing the final clause")

    

def main():
    while True:
        trydemo()



main()
    
