import random

with open("exercici10/archvivo.txt", "w") as archivo:
        numeroAleatorio = random.randrange(100)
        archivo.write(f"{numeroAleatorio}")
        count = 0
        print("Introduce un número: ")
        numero = input()
        while int(numero) == numeroAleatorio:
                if(int(numero) > numeroAleatorio):
                        print("El número es mas grande")
                        numero = input()
                        count += 1
                else:
                        print("El número es mas pequeño")
                        numero = input()
                        count += 1
        print(f"numero acertado: {numero}, el total de intentos fue: {count}")