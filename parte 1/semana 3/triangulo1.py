# -*- coding: utf-8 -*-
"""
Created on Fri May  7 02:15:48 2021

@author: kelvy
"""

class Triangulo():
    def __init__(self,a,b,c) :
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c
        
    def retangulo(self):
        if self.ladoA > self.ladoB and self.a > self.ladoC:
            if self.ladoA **2 == (self.ladoB**2 + self.ladoC**2):
                return True
        else:
            if self.ladoB > self.ladoC:
                if self.ladoB**2 == (self.ladoA **2 + self.ladoC**2):
                    return True
            else:
                if self.ladoC**2 == (self.ladoB**2 + self.ladoA **2):
                    return True
            return False