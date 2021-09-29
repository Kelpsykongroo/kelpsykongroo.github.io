# -*- coding: utf-8 -*-
"""
Created on Wed May 12 01:54:07 2021

@author: kelvy
"""

def ordenada(lista):

    if len(lista) < 2:
        return True
    
    if lista[0]>lista[1]: #Crescente
        for i in range(len(lista)-1):
            
            if lista[i]<lista[i+1]:
                return False
    if lista[0]<lista[1]: #Decrescente
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                return False
    return True
    