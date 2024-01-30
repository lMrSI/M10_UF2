diccionario = {}

print("Ingrese nombres y edades. Ingrese 0 para dejar de agregar contactos.")

while True:
    try:
        numero = int(input("Ingrese 0 para dejar de agregar contactos, o cualquier otro número para continuar:"))
        if numero == 0:
            break 

        nombre = input("Ingrese el nombre: ")
        
        if nombre in diccionario:
            print("El nombre ya existe en el diccionario. Ingrese otro nombre.")
        else:
            edad = int(input("Ingrese la edad: "))
            diccionario[nombre] = edad
            print("Diccionario:", diccionario)

    except ValueError:
        print("¡Error! Ingrese un número válido.")

print("Diccionario final:", diccionario)
