#Python的递归函数
'''
Python的最大递归调用深度为900多次

构造递归函数需要基例，基例就是递归终点，基例不进行递归

'''
#递归实现 n!
def fact(n):
    if n==0:
        return 1;
    else:
        return fact(n-1)*n


#递归实现 字符串反转
def reverseStr(str):
    if str == "":
        return ""
    else:
        return reverseStr(str[1:])+str[0]

def main():
    print("result is:",reverseStr("Hello"))




main()
