# -*- coding: utf-8 -*-
"""
Created on Wed May  5 06:22:41 2021

@author: kelvy
"""

def dimensoes(matriz):
    return len(matriz),len(matriz[0])

def sao_multiplicaveis(m1, m2):
    tamanho1= dimensoes(m1)
    tamanho2 = dimensoes(m2)
    if tamanho1[1]==tamanho2[0]:
        return True
    else:
        return False