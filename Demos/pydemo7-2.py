# -*- coding: cp936 -*-
'''
使用字典结构合并两个通讯录文本为一个文件
gbk是用来将中文写入文本，防止乱码

'''
'''


'''
def combineFile():
    ftele1 = open('TeleAddressBook.txt','rb') #通过二进制字节流的方式读取文件
    ftele2 = open("EmailAddressBook.txt","rb")

    ftele1.readline()#跳过一行
    ftele2.readline()

    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()

    dic1 = {} #字典方式保存
    dic2 = {}

    for line in lines1: #获取第一个文本中的姓名和电话信息
        elements = line.split()
        #将文本读出来的bytes转换为str类型
        dic1[elements[0]] = str(elements[1].decode("gbk"))

    for line in lines2:#获取第二个文本的姓名和邮件信息
        elements = line.split()
        dic2[elements[0]] = str(elements[1].decode("gbk"))

    #开始处理
    lines = []
    lines.append("姓名\t     电话   \t   邮箱\n")
    '''
    join()函数

    语法：  'sep'.join(seq)

    参数说明
    sep：分隔符。可以为空
    seq：要连接的元素序列、字符串、元组、字典
    上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串

    返回值：返回一个以分隔符sep连接各个元素后生成的字符串


    通过使用join方法加深了对join的理解
    eg：s = char.join([,,,])的作用就是将列表里的元素们连接起来，并用char来分隔而
        组成的新的字符串

    '''
    for key in dic1:
        s = ''
        if key in dic2.keys():
            s = '\t'.join([str(key),dic1[key],dic2[key]])
            s+='\n'
        else:
            s = '\t'.join([str(key),dic1[key],'----------------'])
            s+='\n'
        lines.append(s)

    for key in dic2:
        s = ''
        if key not in dic1.keys():
            s = '\t'.join([str(key),'-----------',dic2[key]])
            s+='\n'
        lines.append(s)

    ftele3 = open("AddressBook.txt",'w')
    ftele3.writelines(lines)

    ftele3.close()  
    ftele1.close()
    ftele2.close()  
        
def main():
    combineFile()
    print("All Done")

main()
