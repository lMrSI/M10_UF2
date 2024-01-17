dict = {}
print("Ingrese nombres y edades: ")
numero = input()
while  int(numero) != 0:
    print("Ingrese la nombre: ")
    nombre = input()
    if(dict.values(nombre) == True):
        print("El nombre ya existe, ingrese otro distinto")
    print("Ingrese la edad: ")
    edad = input()
    dict[nombre] = edad

    print(dict)
    numero = input()
