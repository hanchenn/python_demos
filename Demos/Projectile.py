# -*- coding: cp936 -*-
#�������ʵ������ģ��Ǧ����й켣�������ļ�
from math import sin,cos,radians

class Projectile:
    #self ��ʾ Projectile���������
    def __init__(self,angle,velocity,height):
        #���ݸ����ķ���Ƕȣ���ʼ�ٶȺ�λ�ô���һ��Ͷ�������
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self,time):
        #����Ͷ�����״̬
        self.xpos = self.xpos + time * self.xvel
        yvell = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvell)/2.0
        self.yvel = yvell

    def getY(self):
        #����Ͷ����ĸ߶�
        return self.ypos

    def getX(self):
        return self.xpos
