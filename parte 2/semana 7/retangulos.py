# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 04:25:00 2021

@author: kelvy
"""

l= int(input('digite a largura: '))
a= int(input('digite a altura: '))

 
c1=0

while(a>c1):
    c2=0    
    while(l>c2):
        if(c2==l-1):
            print('#')
        else: 
            if(c1==0 or c1==a-1 or c2==0):
                print('#', end='')
            else:
                print(' ', end='')
        c2=c2+1
    c1=c1+1
        
        