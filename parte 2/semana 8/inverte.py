# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:03:14 2021

@author: kelvy
"""
lista = []
n = 1
while(n):
    n = int(input('Digite um número: '))
    if n:
        lista.append(n)
print()
for i in range(len(lista)):
    print(lista[-(i+1)])