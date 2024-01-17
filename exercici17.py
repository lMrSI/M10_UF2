print("Introduce una frase: ")
entrada = input()
tupla_caracteres_unicos = tuple(set(entrada.replace(" ", "")))
print("Tupla con caracteres únicos:", tupla_caracteres_unicos)
