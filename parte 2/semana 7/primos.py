# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:34:36 2021

@author: kelvy
"""

def n_primos(n):
    total = 0
    c=2
    while n>=c:
        p=2
        b= True
        while c>p:
            if not c%p:
                b=False
            p=p+1
        if b:
            total=total+1
        c=c+1
    return total
                
        