#Condiciones if elif else
#Nos permite evaluar expresiones boleanas que debe cumplirse realizar
#Una accion y en caso de que no entonces relaizan un entero


age=int(input("Ingresa tu edad: "))
genre=int(input("Ingresa H si eres hombre y M si eres mujer: "))
mujer=""
if genre=="M":
    mujer="a"
if age<2:
        print(f"Eres un{mujer} bebe:")
elif age<12:
        print("Eres un joven") 
elif age<18:
        print("Eres un adulto")
elif age>49:
        print("Eres un adulto")  
elif age<50:
        print("Eres un mayor")         
else: 
        print("Eres muy mayor") 
     



