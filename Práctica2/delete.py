import connection as conn

def delete():
    sql_delete = '''    DELETE FROM public.peliculas 
                        WHERE id = 1
    '''
    conn.cursor.execute(sql_delete)
    conn.conn.commit()