# -*- coding: cp936 -*-
'''
字典 的课后练习

'''

# 1. 理解文本和二进制打开方式的区别
def test1():
    f = open("test.txt","r")
    for line in f:
        print(line)    
    f.close()

    f2 = open("test.txt","rb")
    for line in f2:
        print(line)
    f2.close()

    '''
    Output is:
    中国是一个伟大的国家！
    中国是一个伟大的国家！
    
    '''
# 2. 文件处理
def processFile():
    fo = open("AddressBook.txt","r")
    for line in fo:
        #处理一行数据
        print(line)
    fo.close()
    '''
    Output:
    
    姓名	     电话   	   邮箱

    王颐笳	13691177890	57320009@qq.com

    张三	13529293939	----------------

    桑迪	13010026896	wqweqe@163.com

    李斯	15811589981	112211212@qq.com

    王五	-----------	949495968@qq.com

    '''
    
def main():
    #test1()
    #processFile()

main()
