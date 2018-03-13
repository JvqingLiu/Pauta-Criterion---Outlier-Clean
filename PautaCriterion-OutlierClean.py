# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:02:02 2018

@author: liang
"""

# 3sigma criterion
from math import *

def Pauta(x, m, j=1):
    print("-----------------------------")
    print("Round: ", j) # 计算的轮数
    
    def calc_sigma(x): # calculate mean, sigma
        s = 0
        n = len(x)
        for xi in x:
            s = xi + s          
        global x_mean
        x_mean = s / n
        
        print("Number of data: ", n)
        print("Mean: ", x_mean)
       
        # Calculate Sigma 计算标准偏差
        v2 = 0
        for xi in x:
            vi = xi - x_mean
            v2 = pow(vi, 2) + v2
        global sigma # global variable 全局变量
        sigma = sqrt(v2 / (n-1))
        v = v2 / n
        print("Sigma: ", sigma)
        return x_mean, sigma
    # Find bad data
    calc_sigma(x)
    
    bool1 = 1
    for xi in x:
        if abs(xi - x_mean) > 3 * sigma: # 3 sigma准则
            bool1 = 0
    if m == 0:
        return x
    elif bool1:
        print("No bad data")
        print("\n")
        print("**************************")
        print("Bad data has been cleared!")
        return x            
    else:
        i = 0        
        for xi in x:
            if abs(xi - x_mean) > 3 * sigma:
                i = x.index(xi)
                print("Index of bad data: ", i+1)                
                x.pop(i)
                print("Bad data: ", xi)
    # Recursion 递归
    Pauta(x, m-1, j=j+1)
    
    
