# -*- coding: utf-8 -*-
"""
Created on Wed May 12 02:14:35 2021

@author: kelvy
"""


def ordena(lista):
    for i in range(len(lista)):
        menor = lista[i]
        pos = i
      
        for j in range(i, len(lista)):
            if lista[j] < menor:
                menor = lista[j]
                pos = j
        lista[i], lista[pos] = lista[pos], lista[i]
    return lista