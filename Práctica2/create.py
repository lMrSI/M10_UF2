import connection as conn

def insert():
    sql_insert = '''  INSERT INTO public.peliculas(id, titulo, año, director, pais, puntuacion)
                                  VALUES('1', 'Oppenheimer', '2023', 'Christopher Nolan', 'Estados Unidos', 5.0)
    '''
    conn.cursor.execute(sql_insert)
    conn.conn.commit()