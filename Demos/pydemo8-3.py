# -*- coding: cp936 -*-
#面向对象实例——模拟铅球飞行轨迹
from  Projectile import *
def getInputs():
    a = eval(raw_input("Enter the launch angle(in degrees):"))
    v = eval(raw_input("Enter the initial velocity(in meters/sec):"))
    h = eval(raw_input("Enter the initial height(in meters):"))
    t = eval(raw_input("Enter the time interval:"))
    return a,v,h,t

def main():
    angle,vel,h0,time = getInputs()
    shot = Projectile(angle,vel,h0)
    while shot.getY() >=0:
        shot.update(time)
        #print("haha")
    print("\nDistance traveled:%.1fmeters."%shot.getX())
    
if __name__ == "__main__":
    main()

