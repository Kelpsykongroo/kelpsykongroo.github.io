# -*- coding: utf-8 -*-
"""
Created on Thu May  6 02:43:01 2021

@author: kelvy
"""

def conta_letras(frase, contar="vogais"):
    cont = 0
    if contar == 'vogais':
        
        for i in frase.lower():
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                cont += 1
    else:
        for i in frase.lower():
            if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and ord(i)>=ord('a') and ord(i) <= ord('z'):
                cont += 1
    return cont