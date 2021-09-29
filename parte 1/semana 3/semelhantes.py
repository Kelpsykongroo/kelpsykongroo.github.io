# -*- coding: utf-8 -*-
"""
Created on Fri May  7 02:36:29 2021

@author: kelvy
"""

def ordena(ordem1):
    if ordem1[1] < ordem1[0] and ordem1[1] < ordem1[2]:
            ordem1[1], ordem1[0] = ordem1[0], ordem1[1]
            if ordem1[1] > ordem1[2]:
                ordem1[1], ordem1[2] = ordem1[2], ordem1[1]
    if ordem1[2] < ordem1[0] and ordem1[2] < ordem1[1]:
        ordem1[2], ordem1[0] = ordem1[0], ordem1[2]
        if ordem1[1] > ordem1[2]:
            ordem1[1], ordem1[2] = ordem1[2], ordem1[1]
    if ordem1[1] > ordem1[2]:
            ordem1[1], ordem1[2] = ordem1[2], ordem1[1]
    return ordem1
        
    
class Triangulo():
    def __init__(self,a,b,c) :
        self.a = a
        self.b = b
        self.c = c
        
    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            if self.a **2 == (self.b**2 + self.c**2):
                return True
        else:
            if self.b > self.c:
                if self.b**2 == (self.a **2 + self.c**2):
                    return True
            else:
                if self.c**2 == (self.b**2 + self.a **2):
                    return True
            return False
        
    def semelhantes(self, triangulo):
        triang1 = ordena([self.a, self.b, self.c])
        triang2 = ordena([triangulo.a, triangulo.b, triangulo.c])
        resp = True
        
        if triang1[0]>triang2[0]:     
            for i in range(3):
                if triang1[i]%triang2[i]:
                    resp = False
            return resp
        else:
            for i in range(3):
                if triang2[i]%triang1[i]:
                    resp = False
            return resp
        
    def tipo_lado(self):
        if self.a  == self.b and self.a == self.c:
            return 'equilátero'
        if self.a  == self.b or self.a == self.c:
            return 'isóceles'
        return 'escaleno'
    
    def perimetro(self):
        return self.a + self.b + self.c
            
         
        
        
                
        
        
            
            
                
        
        