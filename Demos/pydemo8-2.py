# -*- coding: cp936 -*-
'''
���������������

�������ģʽ��
1. �ٲ�ģʽ
    ���Ӹ����׶ε�˳����
    ����������������������

2. ����ģ��
    �����ԭ�ͣ��ٷֽ׶ν��в��䣬���Զ����µ���Ʒ����໥����

3. ���ݿ�����Ŀǰ�����еģ�
    ����Ϊ���ġ�������ѭ�򽥽�
    ���������������
    �Ե����ϡ���������ѭ����͹۹��ɡ�������������

    ���õ��������������������
    scrum�����ޱ�̣�XP�������濪����Lean Development������̬ϵͳ����������DSDM����
    ��������������Feature Driver Development����ˮ��������Cristal Clear��

    scrum���͵����ݿ�������
    
    
     
'''

'''
������̵ĳ������
    ����ִ�й���Ϊ�������
    ����Ȼ�ĳ������


'''

'''
�������ĳ������
    �������ԣ�״̬������Ϊ
    �ࣺĳ�����ͼ��ϵ�������
        ���ԣ��౾���һЩ����
        �����������Ϊ
    ��Ķ��壺
        class classname[(������)]:
            [��Ա��������Ա����]

        _init_���캯������ʼ������ĸ�������
        _del_�������������ٶ���

        

'''

class Student:
    def __init__(self,name,hours,qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQpoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudent(infoStr):
    name,hours,qpoints = infoStr.split()
    #print("name,hours,qpoints:",name,hours,qpoints)
    return Student(name,hours,qpoints)

def main():
    #�������ļ�
    filename = raw_input("Enter name the grade file:")
    infile = open(filename,'r')
    #�����ļ��е�һ��ѧ���ļ�¼Ϊbest
    best = makeStudent(infile.readline())

    #�����ļ�ʣ��������
    for line in infile:
        #��ÿһ������ת��Ϊһ����¼
        s = makeStudent(line)
    #�����ѧ����ĿǰGPA��ߵģ����¼����
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    #��ӡGPA�ɼ���ߵ�ѧ����Ϣ
    print "The best student is:",best.getName()
    print "hours:",best.getHours()
    print "GPA:",best.gpa()

if __name__ == '__main__':
    main()

    
    
