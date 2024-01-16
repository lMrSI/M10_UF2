print("Introduce la primera palabra: ")
palabra1 = input()

print("Introduce la segunda palabra: ")
palabra2 = input()

tupla = (palabra1, palabra2)

contador = {}

for palabra in tupla:
    for letra in palabra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1

print("Conteo de letras:")
for letra, count in contador.items():
    print(f"{letra}: {count}")
