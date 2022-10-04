import os
def suma(n1,n2):
    return n1+n2
def resta(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2 == 0:
        n2 = 1
        return n1/n2

if __name__ == '__main__':
    nu1= int(input("Ingresa numero 1: \n"))
    nu2 = int(input("Ingresa numero 2: \n"))
    message= f"\n \nCalculadora: \n Elige una opcion \n 1 - suma \n 2- resta \n 3 - multiplicacion \n 4- division \n 5- Salir \n 6-Cambiar numeros"
    while True:
        opcion= int(input(message))
        if opcion == 1:
            os.system('clear')
            print(f"La suma es {nu1} + {nu2} = {suma(nu1,nu2)}")
            
        elif opcion == 2:
            print(f"La resta es {nu1} - {nu2} = {resta(nu1,nu2)}")
            
        elif opcion == 3:
            print(f"La multiplicacion de {nu1} * {nu2} = {multi(nu1, nu2)}")
            
        elif opcion == 4:
            print(f"La divison de {nu1} / {nu2} = {divide(nu1,nu2)}")
            
        elif opcion == 5:
            print("bye!")
            break
        elif opcion == 6:
            nu1= int(input("Ingresa numero 1: \n"))
            nu2 = int(input("Ingresa numero 2: \n"))