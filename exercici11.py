print("Introduce un número entre 10 y 100")
numero = input()
count = 1
if(int(numero) > 100 | int(numero) < 10):
    print("Introduce un número valido")
else:
    numerosConsecutivos = []
    while(count <= int(numero)):
        numerosConsecutivos.append(count)
        count += 1
        tupla = tuple(numerosConsecutivos)
    print(tupla)


