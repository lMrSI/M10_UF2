import connection as conn

#Definir la consulta SQL para actualizar un registro en la tabla PELICULAS
def update():
    sql_update = '''UPDATE public.peliculas SET puntuacion = 4.9 
                    WHERE id = 1
    '''
    #Ejecutar la consulta update utilizando el cursor de la conexión
    conn.cursor.execute(sql_update)
    #commit para guardar los cambios en la base de datos
    conn.conn.commit()

    #Obtener el número de filas modificadas por la consulta
    result = conn.cursor.rowcount
    #Imprime un mensaje que indica el número de filas modificadas
    print("id modificada: ", result, "Actualización efectuada sin errores")