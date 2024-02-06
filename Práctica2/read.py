import connection as conn

#Definir la consulta SQL para leer registros de la tabla PELICULAS
def read():
    sql_read = '''SELECT id, titulo, año, director, pais, puntuacion
                  FROM public.peliculas
    '''
    #Ejecutar la consulta read utilizando el cursor de la conexión
    conn.cursor.execute(sql_read)
    #Obtener todos los resultados de la consulta
    result = conn.cursor.fetchall()
    #Iterar y mostrar toda la información
    for i in result:
        print("id: ", i[0],)
        print("titulo: ", i[1],)
        print("año: ", i[2],)
        print("director: ", i[3],)
        print("pais: ", i[4],)
        print("puntuacion: ", i[5], "\n")