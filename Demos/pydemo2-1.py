#TempConvert.py
for i in range(10):
    val = input("请输入带温度表示符号的温度值(例如：32C):")
    if val[-1] in ['c','C']:
        f = 1.8*float(val[0:-1]) +32 
        print("转换后的温度为:%.2fF"%f)
    elif val[-1] in ['f','F']:
        c = (float(val[0:-1])-32)/1.8
        print("转换后的温度为:%.2fC"%c)
    else:
        print("输入错误")



#Python的注释
'''
单行注释：以　＃　开头

多行注释：以  三个单引号包围

'''


#Python的缩进
'''
1个缩进==4个空格

缩进用于标明代码之间的层次关系

缩进是Python语言中表明程序框架的唯一手段
'''

#Python中的变量
'''
变量在使用前必须赋值，否则编译器会报错

变量的命名在程序中需要唯一性。

Python的大小写敏感！！！


'''
#Python中的空格
'''
强制使用的场合：
Python中的通过使用空格来表示缩进，这时空格必须不多不少；

在其他场合，空格可以随意使用来提高代码的可读性。

'''

#Python中的输入函数
'''
Input()函数从控制台获得用户的输入。
使用方法：
变量名　＝　input（<提示性文字>)
获得的用户输入以字符串形式保存在变量中

'''


#Python中的字符串
'''
Python中的字符串以单引号或者双引号标识

字符串的长度为L，第一个字符的下标为0或-L；最后一个字符的索引值为L-1或-1

val{0:2] 表示一个[0,2)的区间。

val{0:-1] 就是表示除了最后一个字符的区间。



'''

#Python中的赋值
'''
1.单个赋值

2.同步赋值
    指的是同时给多个变量赋值，即先运算右侧N个表达式，然后同时将表达式的
    结果赋值给左侧的变量们。
    如：m,n = 1+1,2+2
        x,y = y,x  使用同步赋值一行代码实现两个变量值的交换

'''

#Python中的输出语句
'''
print()：以字符串的形式输出变量的值

'''

#一个小例子
'''
num1 = input("Please input a number:")
num2 = input("Please input a number:")
avg = (float(num1)+float(num2))/2
print("The average of the two numbers is:%.3f"%avg)
#The average of the two numbers is:1.500

'''

#Python中的循环语句
'''
for i in range(计数值）
    表达式组
'''







