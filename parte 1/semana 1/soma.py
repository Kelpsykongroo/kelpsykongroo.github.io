# -*- coding: utf-8 -*-
"""
Created on Wed May  5 06:04:25 2021

@author: kelvy
"""

def dimensoes(matriz):
    return len(matriz),len(matriz[0])
    
def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        linha, coluna = dimensoes(m1)
        for i in range(linha):
            for j in range(coluna):
                m1[i][j] = m1[i][j] + m2[i][j]
        return m1
    else:
        return False