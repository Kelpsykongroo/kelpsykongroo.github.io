a=int(input('Digite um número: '))
b=int(input('Digite um número: '))
c=int(input('Digite um número: '))

delta=b**2 - 4*a*c

if(delta==0):
	r=(-b + delta**(1/2))/(2*a)
	print('a raiz desta equação é', r)
else:
	if(delta<0):
		print("esta equação não possui raízes reais")
	else:
		r1=(-b + delta**(1/2))/(2*a)
		r2=(-b - delta**(1/2))/(2*a)
		if(r2>r1):
			print('as raízes da equação são', r1,'e', r2)
		else:
			print('as raízes da equação são', r2,'e', r1)
