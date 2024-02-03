import create_table
import create
import read
import update
import delete

def main():
    opcion = input("Crear una tabla. (Si/No): ")
    try:
        opcion = opcion
    except ValueError: 
        print("Ingresar solo Si o No.")
        return
    if opcion == "Si":
        create_table.create()
    elif opcion == "No":
        print("Tabla no creada.")
    else:
        print("Opción no valida")

    opcion = input("Insertar datos. (Si/No): ")
    try:
        opcion = opcion
    except ValueError: 
        print("Ingresar solo Si o No.")
        return
    if opcion == "Si":
        create.insert()
    elif opcion == "No":
        print("Datos no insertados.")
    else:
        print("Opción no valida")
    
    read.read()

    opcion = input("Actualizar datos. (Si/No): ")
    try:
        opcion = opcion
    except ValueError: 
        print("Ingresar solo Si o No.")
        return
    if opcion == "Si":
        update.update()
    elif opcion == "No":
        print("Datos no actualizados.")
    else:
        print("Opción no valida")

    opcion = input("Borrar datos. (Si/No): ")
    try:
        opcion = opcion
    except ValueError: 
        print("Ingresar solo Si o No.")
        return
    if opcion == "Si":
        delete.delete()
    elif opcion == "No":
        print("Datos no borrados.")
    else:
        print("Opción no valida")
    
    read.read()

if __name__ == "__main__":
    main()