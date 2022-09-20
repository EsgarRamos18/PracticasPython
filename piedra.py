
import random
#Computadora elige la opcion
aletorio= random.randint(1,3)
machine=""
if aletorio==1:
    machine="piedra"
elif aletorio==2:
    machine="papel"   
else:
    machine="tijera"
#Elije el usuario
print("1 Piedra")
print("2 Papel")
print("3 Tijera")
user=int(input("Elige tu opcion"))
elus=""
if user==1:
    elus="piedra"
elif user==2:
    elus="papel"   
else:
    elus="tijera"
print(f"El user elijio {elus}")
print(f"la maquina elijio {machine}")
#cuando ganaste
if machine=="piedra" and elus=="papel":
    print("Ganaste papel")
elif machine=="papel" and elus=="tijera":
    print("Ganaste tijera")
elif machine=="tijera" and elus=="piedra":
    print("Ganaste piedra")
    #Para cuando perdiste
elif machine=="papel" and elus=="piedra":
    print("Perdiste piedra")
elif machine=="tijera" and elus=="papel":
    print("Perdiste papel")
elif machine=="piedra" and elus=="tijera":
    print("Perdiste tijera")
else:
    print("Empate")