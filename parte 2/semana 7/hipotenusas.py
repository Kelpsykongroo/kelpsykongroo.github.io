# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:19:20 2021

@author: kelvy
"""
def hipotenusa(n):
    i=1
    while i<n:
        j=1
        while j<n:
            if n**2==i**2+j**2:
                return True
            j=j+1
        i=i+1
    
def soma_hipotenusas(n):
    total = 0
    while n>1:
        if hipotenusa(n):
            total = total + n
        n=n-1
    return total