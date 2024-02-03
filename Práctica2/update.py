import connection as conn

def update():
    sql_update = '''    UPDATE public.peliculas SET puntuacion = 4.9 
                        WHERE id = 1
    '''

    conn.cursor.execute(sql_update)
    conn.conn.commit()

    result = conn.cursor.rowcount
    print("id modificada: ", result, "Actualización efectuada sin errores")