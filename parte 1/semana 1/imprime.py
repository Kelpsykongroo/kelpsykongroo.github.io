# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def dimensoes(matriz):
    return len(matriz),len(matriz[0])

def imprime_matriz(matriz):
    linha, coluna = dimensoes(matriz)
    for i in range(linha):
        for j in range(coluna):
            if j != coluna-1:
                print(matriz[i][j], end=' ')
            else:
                print(matriz[i][j])