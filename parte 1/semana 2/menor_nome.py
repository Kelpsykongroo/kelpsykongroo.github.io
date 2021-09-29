# -*- coding: utf-8 -*-
"""
Created on Thu May  6 02:22:18 2021

@author: kelvy
"""

def menor_nome(nomes):
    maior = nomes[0]
    for nome in nomes:
        if len(maior) > len(nome.strip()):
            maior = nome.strip()
    return maior.capitalize()