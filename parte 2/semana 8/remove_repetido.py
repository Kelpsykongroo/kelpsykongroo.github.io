# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 18:46:31 2021

@author: kelvy
"""

def remove_repetidos(lista):
    lista.sort()
    nlista = []
    for i in range((len(lista)-1)):
        print(i)
        if lista[i] != lista[i+1]:
            nlista.append(lista[i])
            if i==len(lista)-2:
                nlista.append(lista[i+1])
    return nlista
    
    