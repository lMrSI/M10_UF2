print("Indica entre una y tres palabras: ")
numeroPalabras = input()
if(int(numeroPalabras) == 1):
    palabra = input()
    print(f"La palabra es: {palabra}, tiene: {len(palabra)}, primer caracter: {palabra[0]}, último caracter: {palabra[-1]}")
elif(int(numeroPalabras) == 2):
    primeraPalabra = input()
    segundoPalabra = input()
    print(f"La palabra es: {primeraPalabra}, tiene: {len(primeraPalabra)}, primer caracter: {primeraPalabra[0]}, último caracter: {primeraPalabra[-1]}")
    print(f"La palabra es: {segundoPalabra}, tiene: {len(segundoPalabra)}, primer caracter: {segundoPalabra[0]}, último caracter: {segundoPalabra[-1]}")
elif(int(numeroPalabras) == 3):
    primeraPalabra = input()
    segundoPalabra = input()
    terceraPalabra = input()
    print(f"La palabra es: {primeraPalabra}, tiene: {len(primeraPalabra)}, primer caracter: {primeraPalabra[0]}, último caracter: {primeraPalabra[-1]}")
    print(f"La palabra es: {segundoPalabra}, tiene: {len(segundoPalabra)}, primer caracter: {segundoPalabra[0]}, último caracter: {segundoPalabra[-1]}")
    print(f"La palabra es: {terceraPalabra}, tiene: {len(terceraPalabra)}, primer caracter: {terceraPalabra[0]}, último caracter: {terceraPalabra[-1]}")
else:
    print("Solo entre 1 y 3 palabras")