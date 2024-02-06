import connection as conn

#Definir la consulta SQL para eliminar un registro de la tabla PELICULAS
def delete():
    sql_delete = '''DELETE FROM public.peliculas 
                    WHERE id = 1
    '''
    #Ejecutar la consulta delete utilizando el cursor de la conexión
    conn.cursor.execute(sql_delete)
    #commit para guardar los cambios en la base de datos
    conn.conn.commit()