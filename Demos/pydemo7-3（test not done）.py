# -*- coding: cp936 -*-
'''
�ֵ� �Ŀκ���ϰ

'''

# 1. ����ı��Ͷ����ƴ򿪷�ʽ������
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
    �й���һ��ΰ��Ĺ��ң�
    �й���һ��ΰ��Ĺ��ң�
    
    '''
# 2. �ļ�����
def processFile():
    fo = open("AddressBook.txt","r")
    for line in fo:
        #����һ������
        print(line)
    fo.close()
    '''
    Output:
    
    ����	     �绰   	   ����

    ������	13691177890	57320009@qq.com

    ����	13529293939	----------------

    ɣ��	13010026896	wqweqe@163.com

    ��˹	15811589981	112211212@qq.com

    ����	-----------	949495968@qq.com

    '''
    
def main():
    #test1()
    #processFile()

main()
