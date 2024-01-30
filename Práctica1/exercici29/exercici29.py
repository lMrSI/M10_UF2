def mostrar_numeros_y_suma(num1, num2):
    
    if num1 > num2:
        num1, num2 = num2, num1

    print("Números enteros entre", num1, "y", num2, ":")
    suma = 0
    for i in range(num1, num2 + 1):
        print(i, end=" ")
        suma += i

    print("\nSuma de los números enteros:", suma)

