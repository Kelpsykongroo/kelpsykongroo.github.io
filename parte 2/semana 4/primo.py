n = int(input('Digite um número inteiro: '))
c = 2
primo = True

while(c<n):
    if(n%c == 0):
        primo=False
    c = c+1
if primo:
    print('primo')
else:
    print('não primo')
