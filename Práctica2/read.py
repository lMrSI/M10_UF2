import connection as conn

def read():
    sql_read = '''  SELECT id, titulo, año, director, pais, puntuacion
                    FROM public.peliculas
    '''
    conn.cursor.execute(sql_read)

    result = conn.cursor.fetchall()

    for i in result:
        print("id: ", i[0],)
        print("titulo: ", i[1],)
        print("año: ", i[2],)
        print("director: ", i[3],)
        print("pais: ", i[4],)
        print("puntuacion: ", i[5], "\n")