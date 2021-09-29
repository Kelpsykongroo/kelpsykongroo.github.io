def eprimo(k):
    c=2
    while c<k:
        if k%c==0:
            return False
        c=c+1
    return True
        
def maior_primo(x):
    c=1
    maior = 2
    while (c<=x):
        if eprimo(c):
            maior = c
        c= c+1
    return maior
