# -*- coding: cp936 -*-
'''
ʹ���ֵ�ṹ�ϲ�����ͨѶ¼�ı�Ϊһ���ļ�
gbk������������д���ı�����ֹ����

'''
'''


'''
def combineFile():
    ftele1 = open('TeleAddressBook.txt','rb') #ͨ���������ֽ����ķ�ʽ��ȡ�ļ�
    ftele2 = open("EmailAddressBook.txt","rb")

    ftele1.readline()#����һ��
    ftele2.readline()

    lines1 = ftele1.readlines()
    lines2 = ftele2.readlines()

    dic1 = {} #�ֵ䷽ʽ����
    dic2 = {}

    for line in lines1: #��ȡ��һ���ı��е������͵绰��Ϣ
        elements = line.split()
        #���ı���������bytesת��Ϊstr����
        dic1[elements[0]] = str(elements[1].decode("gbk"))

    for line in lines2:#��ȡ�ڶ����ı����������ʼ���Ϣ
        elements = line.split()
        dic2[elements[0]] = str(elements[1].decode("gbk"))

    #��ʼ����
    lines = []
    lines.append("����\t     �绰   \t   ����\n")
    '''
    join()����

    �﷨��  'sep'.join(seq)

    ����˵��
    sep���ָ���������Ϊ��
    seq��Ҫ���ӵ�Ԫ�����С��ַ�����Ԫ�顢�ֵ�
    ������﷨������sep��Ϊ�ָ�������seq���е�Ԫ�غϲ���һ���µ��ַ���

    ����ֵ������һ���Էָ���sep���Ӹ���Ԫ�غ����ɵ��ַ���


    ͨ��ʹ��join���������˶�join�����
    eg��s = char.join([,,,])�����þ��ǽ��б����Ԫ������������������char���ָ���
        ��ɵ��µ��ַ���

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
