# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:52:33 2021

@author: kelvy
"""

def maior_elemento(lista):
    m=lista[0]
    for i in range(len(lista)-1):
    
        if lista[i+1]>m:
            m=lista[i+1]
    return m
            
            
        