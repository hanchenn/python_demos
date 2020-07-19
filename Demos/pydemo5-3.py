'''
Python中的参数是通过值来传递的。

如果变量是可变的对象，返回到调用程序后，该对象会呈现被修改后的状态

'''

#处理多个银行账户的程序
def addInterest(balances,rate):
    for i in range(len(balances)):
        balances[i] = balances[i]*(1+rate)#由于列表的值可以修改，所以可以这样写

def test():
    amounts = [1000,105,3500,739]
    rate = 0.05
    addInterest(amounts,rate)
    print(amounts)

def changeStr(str):
    for i in range(len(str)):
        print("str is:",str[i])
        str[i] = "a"#执行这一行时，系统报错，因为字符串是常量，不能改动哦
    

def testStr():
    str = "abcd"
    changeStr(str)
    print(str)
    

def main():
    #test()
    testStr()



main()
