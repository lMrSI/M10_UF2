print("Introduce una serie de números: ")
lista = []
numero = input()
while int(numero) != 0:
    lista.append(int(numero))
    numero = input()
lista.sort()
tupla = tuple(lista)
print(tupla)



