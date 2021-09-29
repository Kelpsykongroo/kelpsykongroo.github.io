n = int(input('Digite um número inteiro: '))
t=n%10
condic = True
while(condic and n>0):
    n=n//10
    if(n%10==t):
        condic = False
    else:
        t=n%10
        

if condic:
    print('não')
else:
    print('sim')
