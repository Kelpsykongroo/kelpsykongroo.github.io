# -*- coding: utf-8 -*-
"""
Created on Wed May 12 02:01:01 2021

@author: kelvy
"""

def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
        
    return False