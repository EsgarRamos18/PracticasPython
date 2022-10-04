n1=int(input("Ingresa el numero para crear su tabla de multiplicar: "))
n2=int(input("Ingresa el rango: "))
n2=n2+1
for n2 in range(1,n2):
	multiplicacion = n1 * n2 
	print(f'{n1} x {n2} = {multiplicacion}') 
