print("Introducir un valor en €")
numero = input()
print("Introduce el IVA (4%, 10%, 21%)")
iva = input()

if(iva == str(4)):
    valorFinal = int(numero) * 0.04
    print(f"valor: {numero}, IVA: {iva}, valor final: {valorFinal + int(numero)}")

if(iva == str(10)):
    valorFinal = int(numero) * 0.10
    print(f"valor: {numero}, IVA: {iva}, valor final: {valorFinal + int(numero)}")

if(iva == str(21)):
    valorFinal = int(numero) * 0.21
    print(f"valor: {numero}, IVA: {iva}, valor final: {valorFinal + int(numero)}")
