#Python中的函数
'''
Python中的函数
1.Python内嵌函数：abs(),eval()
2.Python标准库中的函数：math库中的sqrt()
3.图形库中的方法：mypoint.getX()等

Python中函数的定义
def funcName(parameters):
    body

Python中的函数可以返回任何类型，函数没有return语句等价于return None

'''

def happy():
	print("Happy birthday to you~")
def sing(person):
	happy()
	happy()
	#注意python大小写敏感
	print("Happy birthday,dear",person,"!")
	happy()
def main():
	sing("Mike")
	print()#输出空行
	sing("Lily")
	print()
	sing("Elmer")
main()
