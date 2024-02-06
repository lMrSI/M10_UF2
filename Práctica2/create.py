import connection as conn

#Hacer la consulta SQL para insertar un nuevo registro en la tabla PELICULAS
def insert():
    sql_insert = '''  INSERT INTO public.peliculas(id, titulo, año, director, pais, puntuacion)
                                  VALUES('1', 'Oppenheimer', '2023', 'Christopher Nolan', 'Estados Unidos', 5.0)
    '''
    #Ejecutar la consulta insert utilizando el cursor de la conexión
    conn.cursor.execute(sql_insert)
    #commit para guardar los cambios en la base de datos
    conn.conn.commit()