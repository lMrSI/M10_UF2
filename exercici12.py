tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

print("Introduce un número del 0 al 12: ")
numero = input()

while int(numero) != 0:
    print(tupla[:int(numero)])
    numero = input()