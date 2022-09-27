def suma(n1,n2):
    return n1+n2
def resta(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

if __name__ == '__main__':
    message= f"Calculadora: \n Elige una opcion \n 1 - suma \n 2- resta \n 3 - multiplicacion \n 4- division \n 5- Salir"
    while True:
        opcion= int(input(message))
        if opcion == 5:
            print("bye!")
            break