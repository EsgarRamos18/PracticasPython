#Lee la edad de alguien
age_human=int(input("Ingresa tu edad: "))
#Resta 2 a esta edad y se llama last_yers
last_years=age_human-2
#First_years sera igual a los 2 por 10.5
first_years=2*10.5
#Multiplicar los años restantes(last_years) por 4
last_years=last_years*4
#Sumar los first_years con el resultado anterior
age_dog=last_years+first_years
print(f"Tienes {age_human} años que equivalen a {age_dog} años perrunos")

