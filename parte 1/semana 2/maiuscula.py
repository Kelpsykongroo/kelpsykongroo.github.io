# -*- coding: utf-8 -*-
"""
Created on Thu May  6 02:04:48 2021

@author: kelvy
"""

def maiusculas(frase):
    maisc = ''
    for i in range(len(frase)):
        if ord(frase[i])<ord('a') and ord(frase[i])>65:
            maisc = maisc + frase[i]
    return maisc
        