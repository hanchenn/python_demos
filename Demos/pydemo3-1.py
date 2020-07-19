#python 中的数据类型

#数字类型
'''
#python 中的整数类型

Python中的整数没有范围限制
十进制
十六进制，以0x，0X开头
八进制，以0o，0O开头
二进制，以0b，0B开头

'''

'''
#浮点数类型
带小数点的数

科学计数法使用字母“e”或者“E”作为幂的符号，以10为基数
eg：aeb = a乘以10的b次幂


'''

'''
#复数类型

与数学概念一致，z = a + bj，a是实数部分，b是虚数部分，a,b都是浮点类型
虚数部分用j或者J标识。


eg：z = 1.23e-4+5.6e+89j
对于负数z,可以用z.real获得实数部分，z.imag获得虚数部分
z.real = 1.23e-4
z.imag = 5.6e+89

'''

#数字类型的关系
'''
整数、浮点数、复数宽度的比较
整数<浮点数<复数
不同数字类型之间进行混合运算时，运算结果为最宽类型。

数字类型间的互相转换：
int()  eg:int(4.5)=4
float()  eg:float(4)=4.0
complex()   eg:complex(4.0)=4.0+0j

type()函数用于判断数据的类型
'''


#字符串类型
'''
字符串索引从0开始，一个长度为L的字符串最后一个字符的位置是L-1


Python允许使用负数从字符串右边末尾想做进行反向索引，最右侧索引值为-1

可以通过两个索引值确定一个位置范围，返回这个范围的子串
格式：String[start:end] 

字符串的连接：
+　连接

*  连接
eg:3 * 'hello'  ->'hellohellohello'

len()返回字符串长度
多数数据类型可以通过str()函数转换成字符串。eg：str(123.456) -> '123.456'


'''
'''
#month.py
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("Please input the number of month:(1-12):")
pos = (int(n)-1)*3
monthName = months[pos:pos+3]
print("The name of your month is:"+monthName)
'''
'''
#week.py
days = "星期一星期二星期三星期四星期五星期六星期日"
n1 = input("Please input the number of day:(1-7):")
pos1 = (int(n1)-1)*3
dayName = days[pos1:pos1+3]
print("The name of your day is:"+dayName)
'''

#元组类型
'''
元组是包含多个元素的类型，元素之间用逗号分隔。
eg：t1 = 123,456,"hello"
    t2 = ()
    t3 = 123,
元组外侧可以使用括号，也可以不使用

元组的三个特点：
1. 元组中元素可以是不同类型.元组以可以嵌套元组。

2. 元组中的元素有序，可以通过索引访问元素。也可以通过索引区间访问其元素
    元组之间也可以使用+和*进行运算。

3. 元组定以后不能更改，也不能删除




'''


#列表类型
'''
列表list是有序的元素集合

与元组类似，列表中每个元素类型可以可不一样，可以用索引形式访问元素，

与元组不同的是，列表的大小和内容没有限制可以随时修改


'''
#列表的一些操作
vlist = [0,1,2,3,4]
print("vlist is:",vlist)

vlist*=2
print("vlist*2 is:",vlist)


length = len(vlist[2:])
print("length is :",length)

for i in vlist[:3]:
    print(i)


print(2 in vlist)
