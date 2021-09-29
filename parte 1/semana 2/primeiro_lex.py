# -*- coding: utf-8 -*-
"""
Created on Thu May  6 02:53:14 2021

@author: kelvy
"""

def  primeiro_lex(lista):
    maior = lista[0]
    for i in lista:
        if i < maior:
            maior = i
    return maior