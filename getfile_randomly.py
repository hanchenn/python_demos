# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:45:36 2020

@author: whc
"""
import random
def read_txt(txt_path):
    f = open(txt_path,"r")   
    data_list = f.readlines()
    f.close()         
    return data_list

def randm_list(num_list,rscale):
    new_num_list = []
    for num in num_list:
        rd =(random.randint(0,rscale*100))/100*(-1)**(random.randint(0,4))
        new_num_list.append(float(num[:-1]) + rd)
    return new_num_list
    
def print_list(l):
    for ll in l:
        print(ll)
    
def main():
    txt_path = "vv.txt"
    rscale = 6
    print_list(randm_list(read_txt(txt_path),rscale))
    
main()