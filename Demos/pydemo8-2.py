# -*- coding: cp936 -*-
'''
软件开发方法基础

软件开发模式：
1. 瀑布模式
    重视各个阶段的顺序性
    开发进程容易阻塞，代价

2. 螺旋模型
    先设计原型，再分阶段进行补充，与自顶向下的设计方法相互补充

3. 敏捷开发（目前最流行的）
    以人为核心、迭代、循序渐进
    符合软件开发规律
    自底向上、逐步有序、遵循软件客观规律、迭代增量开发

    常用的轻量级软件开发方法：
    scrum、极限编程（XP）、精益开发（Lean Development）、动态系统开发方法（DSDM）、
    特征驱动开发（Feature Driver Development）、水晶开发（Cristal Clear）

    scrum典型的敏捷开发方法
    
    
     
'''

'''
面向过程的程序设计
    程序执行过程为设计流程
    最自然的程序设计


'''

'''
面向对象的程序设计
    对象：属性（状态）、行为
    类：某种类型集合的描述。
        属性：类本身的一些特征
        方法：类的行为
    类的定义：
        class classname[(父类名)]:
            [成员函数及成员变量]

        _init_构造函数：初始化对象的各个属性
        _del_析构函数：销毁对象

        

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
    #打开输入文件
    filename = raw_input("Enter name the grade file:")
    infile = open(filename,'r')
    #设置文件中第一个学生的记录为best
    best = makeStudent(infile.readline())

    #处理文件剩余行数据
    for line in infile:
        #将每一行数据转换为一条记录
        s = makeStudent(line)
    #如果该学生是目前GPA最高的，则记录下来
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    #打印GPA成绩最高的学生信息
    print "The best student is:",best.getName()
    print "hours:",best.getHours()
    print "GPA:",best.gpa()

if __name__ == '__main__':
    main()

    
    
