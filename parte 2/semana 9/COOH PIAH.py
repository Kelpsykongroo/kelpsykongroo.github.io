# -*- coding: utf-8 -*-
"""
Created on Tue May  4 02:28:55 2021

@author: kelvy
"""

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    grau_similiraidade = 0.0
    for i in range(6):
        grau_similiraidade = grau_similiraidade + abs(as_a[i]-as_b[i])/6
    return grau_similiraidade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    sentenças = separa_sentencas(texto)
    frases = []
    for sentença in sentenças:
        frases = frases + separa_frases(sentença)
    palavras = []
    for frase in frases:
        palavras = palavras + separa_palavras(frase)
    return[tamanho_medio_palavras(palavras), calcula_type_token(palavras), hapax_legomana(palavras), tamanho_medio_frase(sentenças), complexidade_setença(sentenças, frases), tamanho_medio_frase(frases)]
    
def calcula_type_token(palavras):
    ''' palavrasSemRepetir = []
    for palavra in palavras:
        if not palavra.lower() in palavrasSemRepetir:
            palavrasSemRepetir.append(palavra.lower())
    return len(palavrasSemRepetir)/len(palavras) '''

    return n_palavras_diferentes(palavras)/len(palavras)
    
def tamanho_medio_palavras(palavras):
    tamanhoMedioPalavras = 0
    for palavra in palavras:
        tamanhoMedioPalavras = tamanhoMedioPalavras + len(palavra)/len(palavras)

    return tamanhoMedioPalavras
    
def hapax_legomana(palavras):
    ''' palavrasSemRepetir = []
    for i in range(len(palavras)):
        if (not palavras[i] in palavras[i+1:]) or (not palavras[i] in palavras[:i]):
            palavrasSemRepetir.append(palavras[i])
    return len(palavrasSemRepetir)/len(palavras) '''

    return n_palavras_unicas(palavras)/len(palavras)

def tamanho_medio_sentença(sentenças):
    ''' Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).'''
    tamanhoMedioSentença = 0
    for sentença in sentenças:
        tamanhoMedioSentença = tamanhoMedioSentença + len(sentença)
    tamanhoMedioSentença =  tamanhoMedioSentença/(len(sentenças))
    return tamanhoMedioSentença

def complexidade_setença(sentença,frases):
    ''' Complexidade de sentença é o número total de frases divido pelo número de sentenças. '''
    return len(frases)/len(sentença)

def tamanho_medio_frase(frases):
    ''' Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto  (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase). '''
    '''separa_palavras(frase)
        tamanhoMedioPalavras = 0
            for palavra in palavras:
                tamanhoMedioPalavras = tamanhoMedioPalavras + len(palavra)
                tamanhoMedioFrase = tamanhoMedioFrase + len(frase)
            '''
    tamanhoMedioFrase = 0
    for frase in frases:
        tamanhoMedioFrase = tamanhoMedioFrase + len(frase)/len(frases)
    return tamanhoMedioFrase
        

def avalia_textos(textos, ass_cp):
    
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    probabilidade = []
    for texto in textos:
        as_a = calcula_assinatura(texto)
        probabilidade.append(compara_assinatura(as_a,ass_cp))
    
    maior = probabilidade[0]
    t = 0
    for i in range(len(probabilidade)):
        if probabilidade[i] < maior:  
            t=i
            maior = probabilidade[i]
    return t+1  