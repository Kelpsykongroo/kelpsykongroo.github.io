# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 17:55:07 2021

@author: kelvy
"""
def resta(p):
    if(p!=0):
        if p>1:
            print('Agora restam', p, 'peças no tabuleiro.')
            print()
        else:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
            
    
def computador(p,l):
    """vez do computador"""
    m=p
    if p<l:
        print('O computador tirou', p, 'peças')
        return p
    while (m%(l+1)!=0):
        m=m-1
    if (p-m)>l:
        if l>1:
            print('O computador tirou uma peça')
        else:
            print('O computador tirou', p ,'peças')
        resta(p-l)
        print()
        p=p-1
        return p
    else:
        print('O computador tirou', p-m, 'peça')
        resta(m)
        return m

def jogador(p,l):
    """vez do jogador"""
    t=int(input('Quantas peças você vai tirar? '))
    while t>l:
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        t=int(input('Quantas peças você vai tirar? '))
    p=p-t
    resta(p)
    return p
        
    
    
def partida():
    """gerencia a partida"""
    p=int(input('Quantas peças? '))
    l=int(input('Limite de peças por jogada? '))
    print()
    
    if (l+1)%p:
        print('Computador começa!')
        print()
        while(p>0):
            p=computador(p,l)
            if p==0:
                print('Fim do jogo! O computador ganhou!')
                print()
                return True
            p=jogador(p,l)
            if p==0:
                print('Fim do jogo! Você ganhou ganhou!')
                print()
                return False
    else:
        print('Você começa!')
        while(p>l):
            p=jogador(p,l)
            if p==0:
                print('Fim do jogo! Você ganhou ganhou!')
                return False
            p=computador(p,l)
            if p==0:
                print('Fim do jogo! O computador ganhou!')
                print()
                return True
            
              
        
"""começo do jogo"""
print('Bem-vindo ao jogo do NIM! Escolha:')
t= input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato ')      
if t=='1':
    partida()
else:
    print()
    print('Voce escolheu um campeonato!')
    print()
    x=0
    pj = 0
    pc = 0
    while(3>x):
        print('**** Rodada',x+1,'****')
        if partida():
            pc=pc+1
        else:
            pj=pj+1
        x=x+1
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você', pj,'X', pc, 'Computador')
    
    
