numeros = input("Introducir 10 números: ")

numero = [int(num) for num in numeros.split()]
if len(numero) == 10:
    #numero.sort()
    tupla = tuple(sorted(numero))
    print(tupla)

    
