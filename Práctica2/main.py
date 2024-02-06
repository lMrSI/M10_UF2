import create_table
import create
import read
import update
import delete

def main():
    try:
        #EL usuario elige que desea hacer
        opcion = input("¿Qué consulta desea hacer? (Create = 1, Read = 2, Update = 3, Delete = 4, Insert = 5): ")
        opcion = int(opcion)
        #Crear una tabla
        if opcion == 1:
            opcion = input("Crear una tabla. (Si/No): ")
            if opcion.lower() == "si":
                create_table.create()
            elif opcion.lower() == "no":
                print("Tabla no creada.")
            else:
                print("Opción no válida")
        #Leer los datos 
        elif opcion == 2:
            read.read()
        #Actualizar los datos
        elif opcion == 3:
            opcion = input("Actualizar datos. (Si/No): ")
            if opcion.lower() == "si":
                update.update()
                read.read()
            elif opcion.lower() == "no":
                print("Datos no actualizados.")
            else:
                print("Opción no válida")
        #Borrar los datos
        elif opcion == 4:
            opcion = input("Borrar datos. (Si/No): ")
            if opcion.lower() == "si":
                delete.delete()
                read.read()
            elif opcion.lower() == "no":
                print("Datos no borrados.")
            else:
                print("Opción no válida")
        #Insertar los datos
        elif opcion == 5:
            opcion = input("Insertar datos. (Si/No): ")
            if opcion.lower() == "si":
                create.insert()
                read.read()
            elif opcion.lower() == "no":
                print("Datos no insertados.")
            else:
                print("Opción no válida")
        else:
            print("Opción no válida.")
    except Exception as e:
        print("Error:", e)
    finally:
        # Cerrar la conexión al finalizar
        create_table.conn.conn.close()
        create.conn.conn.close()
        update.conn.conn.close()
        delete.conn.conn.close()
        read.conn.conn.close()

if __name__ == "__main__":
    main()

