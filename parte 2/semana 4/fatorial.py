n= int(input('Digite o valor de n: '))

if(n>2):
    total = n
    while(n>1):
        total = total*(n-1)
        n=n-1
    print(total)
else:
    if(n==1 or n == 0):
        print(1)
