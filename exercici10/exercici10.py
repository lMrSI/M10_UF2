
import random


numeroAleatorio = random.randrange(101)

with open("exercici10/archvivo.txt", "w") as archivo:
    archivo.write(f"{numeroAleatorio}")

count = 1

print("Introduce un número: ")
numero = input()

while int(numero) != numeroAleatorio:
    
    if int(numero) > numeroAleatorio:
        print("El número es más pequeño, inténtalo nuevamente")
        numero = input()
        count += 1
    else:
        print("El número es más grande, inténtalo nuevamente")
        numero = input()
        count += 1
print(f"Número acertado: {numero}, el total de intentos fue: {count}")
