print("Introduce un número entre el 1 al 10")

numero = input()
if int(numero) > 10:
    print("Introduce un número correcto: ")
else:
    print("Resultado")
    count = 1
    while count != 11:
        resultado = int(numero) * count
        count += 1
        print(resultado)



