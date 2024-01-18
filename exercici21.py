numeros = input("Introducir 10 números: ")
suma = 0
media = 0
numero = [int(num) for num in numeros.split()]
if len(numero) == 10:
    list = (numero)
    print(f"Números del usuario: {list}")
    for numerosUsuarios in list:
        suma += numerosUsuarios
        media = suma / 2
    print(f"Suma total: {suma}")
    print(f"Media: {media}")