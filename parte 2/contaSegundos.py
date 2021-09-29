segundos = float(input("Por favor, entre com o número de segundos que deseja converter:"))
d=int(segundos//86400)
h=int((segundos%86400)//3600)
m=int(((segundos%86400)%3600)//60)
s=int(((segundos%86400)%3600)%60)

print(d,"dias,",h,"horas,",m,"minutos e",s,"segundos.")
